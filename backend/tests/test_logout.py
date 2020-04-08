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


def test_logout_user_with_valid_access_token(auth_client):
    """Test logout with fresh access token."""
    response = auth_client.delete("/auth/logout/")
    payload = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert payload["msg"] == "Successfully logged out"


@pytest.mark.parametrize("url", ["/auth/logout/", "/auth/refresh-token/"])
def test_logout_user_without_token(client, url):
    """Test logout with no token provided."""
    response = client.delete("/auth/logout/")
    payload = response.get_json()
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert payload["msg"] == "Missing Authorization Header"


def test_logout_twice(app, auth_client):
    """Test logout twice."""
    with app.app_context():
        response = auth_client.delete("/auth/logout/")
        assert response.status_code == HTTPStatus.OK
        response = auth_client.delete("/auth/logout/")
        tokens = JWTToken.query.all()
    payload = response.get_json()
    assert tokens[0].revoked
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert payload["msg"] == "Token has been revoked"


def test_get_protected_route_after_logout(protected_route, auth_client):
    """Test access protected route after logging out."""
    response = auth_client.delete("/auth/logout/")
    assert response.status_code == HTTPStatus.OK
    response = auth_client.get("/")
    payload = response.get_json()
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert payload["msg"] == "Token has been revoked"


def test_revoke_refresh_token(client, tokens):
    """Test revoke refresh token."""
    response = client.delete(
        "/auth/refresh-token/",
        headers={"Authorization": f"Bearer {tokens['refresh']}"},
    )

    payload = response.get_json()
    assert response.status_code == HTTPStatus.OK
    assert payload["msg"] == "Refresh token successfully revoked"
