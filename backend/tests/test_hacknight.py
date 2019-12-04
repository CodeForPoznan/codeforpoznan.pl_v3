from http import HTTPStatus


def test_get_hacknights_when_logged_in(client, access_token, add_hacknights):
    """Test get list of hacknights for logged in user."""
    rv = client.get(
        "/hacknights/", headers={"Authorization": "Bearer {}".format(access_token)}
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert len(response["hacknights"]) == 10


def test_get_hacknights_with_empty_db(client, access_token):
    """Test get list of hacknights when no hacknight added to db."""
    rv = client.get(
        "/hacknights/", headers={"Authorization": "Bearer {}".format(access_token)}
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not response["hacknights"]


def test_get_hacknights_unauthorized(client, add_hacknights):
    """Test get list of hacknights when user is not logged in."""
    rv = client.get("/hacknights/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"
