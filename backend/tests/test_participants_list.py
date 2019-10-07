from http import HTTPStatus

from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema


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


def test_create_participant_when_logged_in(
    app, client, access_token, new_participant
):
    """Test create new participant with logged in user and valid data."""
    with app.app_context():
        rv = client.post(
            '/participants/',
            headers={'Authorization': 'Bearer {}'.format(access_token)},
            json=new_participant
        )

        response = rv.get_json()
        schema = ParticipantSchema()
        participant = schema.dump(Participant.query.first())

    assert rv.status_code == HTTPStatus.CREATED
    assert response["participant"]["email"] == new_participant["email"]
    for value in new_participant.values():
        assert value in participant.values()


def test_try_create_participant_without_payload(client, access_token):
    """Test try to create new participant without payload."""
    rv = client.post(
        '/participants/',
        headers={'Authorization': 'Bearer {}'.format(access_token)},
        json={}
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response['message'] == 'No input data provided'


def test_try_create_participant_with_invalid_email(
    client, access_token, new_participant
):
    """Test try to create new participant with invalid email address."""
    new_participant['email'] = "test"

    rv = client.post(
        '/participants/',
        headers={'Authorization': 'Bearer {}'.format(access_token)},
        json=new_participant
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert 'Not a valid email address.' in response['email']


def test_try_create_participant_without_name(
    client, access_token, new_participant
):
    """Test try create new participant without name."""
    del new_participant['name']

    rv = client.post(
        '/participants/',
        headers={'Authorization': 'Bearer {}'.format(access_token)},
        json=new_participant
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert 'Missing data for required field.' in response['name']


def test_create_participant_unauthorized(client, new_participant):
    """Test create new participant when user is not logged in."""
    rv = client.post('/participants/', json=new_participant)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == 'Missing Authorization Header'
