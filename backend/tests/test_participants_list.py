from http import HTTPStatus

from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema


def test_get_participants_when_logged_in(auth_client, add_participants):
    """Test get participants list for logged in user."""
    rv = auth_client.get("/participants/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert len(response) == 10


def test_get_participants_with_empty_db(auth_client):
    """Test get participants list when no participant in db."""
    rv = auth_client.get("/participants/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not response


def test_get_participants_unauthorized(client, add_participants):
    """Test get participants list when user is not logged in."""
    rv = client.get("/participants/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


def test_create_participant_when_logged_in(app, auth_client, new_participant):
    """Test create new participant with logged in user and valid data."""
    with app.app_context():
        rv = auth_client.post("/participants/", json=new_participant)

        response = rv.get_json()
        schema = ParticipantSchema()
        participant = schema.dump(Participant.query.first())

    assert rv.status_code == HTTPStatus.CREATED
    assert response["email"] == new_participant["email"]
    for value in new_participant.values():
        assert value in participant.values()
    for value in participant.keys():
        assert value in response


def test_try_create_participant_without_payload(auth_client):
    """Test try to create new participant without payload."""
    rv = auth_client.post("/participants/", json={})
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["message"] == "No input data provided"


def test_try_create_participant_with_invalid_email(auth_client, new_participant):
    """Test try to create new participant with invalid email address."""
    new_participant["email"] = "test"

    rv = auth_client.post("/participants/", json=new_participant)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert "Not a valid email address." in response["email"]


def test_try_create_participant_without_first_name(auth_client, new_participant):
    """Test try create new participant without name."""
    del new_participant["first_name"]

    rv = auth_client.post("/participants/", json=new_participant)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST

    assert "Missing data for required field." in response["first_name"]


def test_create_participant_unauthorized(client, new_participant):
    """Test create new participant when user is not logged in."""
    rv = client.post("/participants/", json=new_participant)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


def test_try_create_participant_with_existing_email(auth_client, new_participant, _db):
    """Test try to create new participant with existing email address."""
    db = _db
    participant = Participant(**new_participant)
    db.session.add(participant)
    db.session.commit()

    payload = {
        "first_name": "JonX",
        "last_name": "DoeX",
        "email": "test@test.com",
        "phone": "1234567890",
        "github": "wihajsterX",
    }
    rv = auth_client.post("/participants/", json=payload)
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.CONFLICT
    assert "User with this email already exists." in response["message"]


def test_try_create_participant_with_existing_github(auth_client, new_participant, _db):
    """Test try to create new participant with existing github nickname."""
    db = _db
    participant = Participant(**new_participant)
    db.session.add(participant)
    db.session.commit()

    payload = {
        "first_name": "JonX",
        "last_name": "DoeX",
        "email": "test@test.com2",
        "phone": "1234567890",
        "github": "wihajster",
    }
    rv = auth_client.post("/participants/", json=payload)
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.CONFLICT
    assert "User with this Github login already exists." in response["message"]
