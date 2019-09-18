from http import HTTPStatus
import json

from backend.models import Hacknight, Participant


def test_get_hacknights_when_logged_in(
    client, access_token, add_hacknights
):
    """Test get list of hacknights for logged in user."""
    rv = client.get(
        '/hacknights/',
        headers={'Authorization': 'Bearer {}'.format(access_token)}
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert len(response['hacknights']) == 10


def test_get_hacknights_with_empty_db(client, access_token):
    """Test get list of hacknights when no hacknight added to db."""
    rv = client.get(
        '/hacknights/',
        headers={'Authorization': 'Bearer {}'.format(access_token)}
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not response['hacknights']


def test_get_hacknights_unauthorized(client, add_hacknights):
    """Test get list of hacknights when user is not logged in."""
    rv = client.get('/hacknights/')
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response['msg'] == 'Missing Authorization Header'


def test_add_participants_to_hacknight(
    access_token, add_hacknights, add_participants, client
):
    """Test add new participant to hacknight."""
    payload = {'participants': [1, 3]}
    rv = client.patch(
        '/hacknights/1/',
        headers={'Authorization': 'Bearer {}'.format(access_token)},
        data=json.dumps(payload)
    )
    resp = rv.get_json()
    participants_ids = [
        participant['id'] for participant in resp['hacknight']['participants']
    ]
    assert rv.status_code == HTTPStatus.OK
    for participant in resp['hacknight']['participants']:
        assert participant['id'] in payload['participants']


def test_add_participants_to_hacknight_unauthorized(
    add_hacknights, add_participants, client
):
    """Test add participants to hacknight when user is not logged in."""
    payload = {'participants': [1, 3]}
    rv = client.patch('/hacknights/1/', data=json.dumps(payload))
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response['msg'] == 'Missing Authorization Header'


def test_add_nonexisting_participants_to_hacknight(
    access_token, add_hacknights, client
):
    """Test add non-existing participants ids to hacknight."""
    payload = {'participants': [1, 3]}
    rv = client.patch(
        '/hacknights/1/',
        headers={'Authorization': 'Bearer {}'.format(access_token)},
        data=json.dumps(payload)
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.NOT_FOUND


def test_add_participants_to_non_existing_hacknight(
    access_token, add_participants, client
):
    """Test add participants to non-existent hacknight."""
    payload = {'participants': [1, 3]}
    rv = client.patch(
        '/hacknights/1/',
        headers={'Authorization': 'Bearer {}'.format(access_token)},
        data=json.dumps(payload)
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.NOT_FOUND


def test_duplicate_participant_in_hacknight(
    access_token, add_hacknights, add_participants, client, _db
):
    """Test add participant who is already in hacknight.."""
    hacknight = _db.session.query(Hacknight).first()
    participant = _db.session.query(Participant).first()
    hacknight.participants.append(participant)

    payload = {'participants': [participant.id]}
    rv = client.patch(
        '/hacknights/{}/'.format(hacknight.id),
        headers={'Authorization': 'Bearer {}'.format(access_token)},
        data=json.dumps(payload)
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response['message'] == 'No new participant has been provided'
