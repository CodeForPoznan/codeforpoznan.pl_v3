from http import HTTPStatus

from backend.models import Participant


def test_get_participants_when_logged_in(
        client, access_token, add_participants
     ):
    """Test get participants list for logged in user."""
    rv = client.get(
        '/participants/',
        headers={'Authorization': 'Bearer {}'.format(access_token)}
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert len(response["participants"]) == 10


def test_get_participants_with_empty_db(client, access_token):
    """Test get participants list when no participant in db."""
    rv = client.get(
        '/participants/',
        headers={'Authorization': 'Bearer {}'.format(access_token)}
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not response["participants"]


def test_get_participants_unauthorized(client, add_participants):
    """Test get participants list when user is not logged in."""
    rv = client.get('/participants/')
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == 'Missing Authorization Header'
