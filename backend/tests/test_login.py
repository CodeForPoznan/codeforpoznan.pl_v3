from http import HTTPStatus

import pytest


def test_login_with_valid_user_admin(client, new_user_admin, registered_user):
    """Test logging with valid data."""
    new_user_dict = {
        k: v
        for k, v in new_user_admin.items()
        if k == ("github_username") or k == ("password")
    }
    rv = client.post("/api/auth/login/", json=new_user_dict)

    response = rv.get_json()
    assert rv.status_code == HTTPStatus.CREATED
    assert response["access_token"]
    assert response["refresh_token"]


def test_login_with_non_admin_user(client, new_user, registered_user):
    """Make sure that only admin can login."""
    new_user_dict = {
        k: v
        for k, v in new_user.items()
        if k == ("github_username") or k == ("password")
    }
    rv = client.post("/api/auth/login/", json=new_user_dict)

    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Not authorized"


def test_refresh_access_token(client, tokens):
    """Test refresh access token with refresh token."""
    rv = client.post(
        "/api/auth/refresh/",
        headers={"Authorization": f"Bearer {tokens['refresh']}"},
    )

    response = rv.get_json()
    assert rv.status_code == HTTPStatus.CREATED
    assert response["access_token"]


def test_login_with_invalid_password(client, new_user_admin, registered_user):
    """Test logging with invalid password."""
    rv = client.post(
        "/api/auth/login/",
        json={
            "github_username": new_user_admin["github_username"],
            "password": "WrongPassword",
        },
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Not authorized"


def test_login_with_invalid_name_password(client):
    """Test logging with invalid name and password."""
    rv = client.post(
        "/api/auth/login/",
        json={"github_username": "WrongName", "password": "WrongPassword"},
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Not authorized"


def test_try_login_twice(client, new_user_admin, tokens):
    """Test try login these same user twice."""
    rv = client.post(
        "/api/auth/login/",
        json=new_user_admin,
        headers={"Authorization": f"Bearer {tokens['access']}"},
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert "User already logged in" in response["msg"]


def test_login_with_invalid_input(client):
    """Test try login with too short github."""
    rv = client.post(
        "/api/auth/login/", json={"github_username": "ab", "password": "pass"}
    )
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert "Wrong input data" in response["msg"]
    assert "Shorter than minimum length" in response["errors"]["github_username"][0]


@pytest.mark.parametrize("missing", ["github_username", "password"])
def test_login_with_one_value_missing(client, missing, new_user):
    """Test try to login without password or github in payload."""
    new_user.pop(missing)
    rv = client.post("/api/auth/login/", json=new_user)

    response = rv.get_json()
    errors = response["errors"][missing]
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert "Wrong input data" in response["msg"]
    assert "Missing data for required field." in errors[0]


def test_login_without_request_body(client):
    """Test login without request body."""
    rv = client.post("/api/auth/login/")
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert "No input data provided" in response["msg"]
