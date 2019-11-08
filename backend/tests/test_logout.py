from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required
import pytest

from backend.models import JWTToken


@pytest.fixture
def protected_route(app):
    @app.route("/", methods=['GET'])
    @jwt_required
    def protected():
        return jsonify({"msg": "That it proteced route"})


def test_logout_user_with_valid_access_token(client, access_token):
    """Test logout with fresh access token."""
    rv = client.delete('/auth/logout/',
                       headers={'Authorization': 'Bearer {}'
                                .format(access_token)})
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert response['msg'] == 'Successfully logged out'


def test_logout_user_without_token(client):
    """Test logout with no token provided."""
    rv = client.delete('/auth/logout/')
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response['msg'] == 'Missing Authorization Header'


def test_logout_twice(app, client, access_token):
    """Test logout twice."""
    with app.app_context():
        rv = client.delete('/auth/logout/',
                           headers={'Authorization': 'Bearer {}'
                                    .format(access_token)})
        assert rv.status_code == HTTPStatus.OK
        rv = client.delete('/auth/logout/',
                           headers={'Authorization': 'Bearer {}'
                                    .format(access_token)})
        tokens = JWTToken.query.all()
    response = rv.get_json()
    assert len(tokens) == 1
    assert tokens[0].revoked
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "token has been revoked"


def test_get_protected_route_after_logout(
    app, client, protected_route, access_token
):
    """Test access protected route after loggin out."""
    rv = client.delete('/auth/logout/',
                       headers={'Authorization': 'Bearer {}'
                                .format(access_token)})
    assert rv.status_code == HTTPStatus.OK
    rv = client.get("/", headers={
        'Authorization': 'Bearer {}'.format(access_token)
    })
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "token has been revoked"
