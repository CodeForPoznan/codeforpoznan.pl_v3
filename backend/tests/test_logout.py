from http import HTTPStatus
import pytest


def test_logout_user_with_valid_access_token(client, access_token):
    """Test logout with fresh access token."""
    rv = client.delete(
        "/auth/logout/", headers={"Authorization": f"Bearer {access_token}"}
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert response["msg"] == "Successfully logged out"


def test_logout_user_without_token(client):
    """Test logout with no token provided."""
    rv = client.delete("/auth/logout/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"
