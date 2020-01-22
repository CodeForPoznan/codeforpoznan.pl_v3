from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required
import pytest

from backend.models import JWTToken


@pytest.fixture
def protected_route(app):
    @app.route("/", methods=["GET"])
    @jwt_required
    def protected():
        return jsonify({"message": "That is protected route"})


def test_logout_user_with_valid_access_token(client, access_token):
    """Test logout with fresh access token."""
    response = client.delete(
        "/auth/logout/", headers={"Authorization": "Bearer {}".format(access_token)}
    )
    payload = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert payload["msg"] == "Successfully logged out"


def test_logout_user_without_token(client):
    """Test logout with no token provided."""
    response = client.delete("/auth/logout/")
    payload = response.get_json()
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert payload["msg"] == "Missing Authorization Header"


def test_logout_twice(app, client, access_token):
    """Test logout twice."""
    with app.app_context():
        response = client.delete(
            "/auth/logout/", headers={"Authorization": "Bearer {}".format(access_token)}
        )
        assert response.status_code == HTTPStatus.OK
        response = client.delete(
            "/auth/logout/", headers={"Authorization": "Bearer {}".format(access_token)}
        )
        tokens = JWTToken.query.all()
    payload = response.get_json()
    assert tokens[0].revoked
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert payload["msg"] == "Token has been revoked"


def test_get_protected_route_after_logout(app, client, protected_route, access_token):
    """Test access protected route after logging out."""
    response = client.delete(
        "/auth/logout/", headers={"Authorization": "Bearer {}".format(access_token)}
    )
    assert response.status_code == HTTPStatus.OK
    response = client.get(
        "/", headers={"Authorization": "Bearer {}".format(access_token)}
    )
    payload = response.get_json()
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert payload["msg"] == "Token has been revoked"
