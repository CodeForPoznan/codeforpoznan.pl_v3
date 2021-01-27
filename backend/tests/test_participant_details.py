from http import HTTPStatus

import pytest

from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema


@pytest.mark.parametrize("method", ["get", "delete"])
def test_get_delete_participant_when_logged_in(
    client, auth_client, add_participants, method
):
    """Test get and delete participant details for logged in user."""
    rv = getattr(auth_client, method)("/api/participants/1/")
    response = rv.get_json()
    participant_schema = ParticipantSchema()
    assert rv.status_code == HTTPStatus.OK
    if method == "get":
        assert response == participant_schema.dump(Participant.query.get(1))
    else:
        assert response["message"] == "Participant deleted successfully."


def test_put_participant_when_logged_in(app, auth_client, add_participants):
    """Test put participant details for logged in user and valid data."""
    with app.app_context():
        payload = {"last_name": "TestTest", "email": "testtest@test.pl"}
        rv = auth_client.put("/api/participants/1/", json=payload,)
        response = rv.get_json()
        schema = ParticipantSchema()
        participant = schema.dump(Participant.query.first())
    assert rv.status_code == HTTPStatus.OK
    assert response["last_name"] == payload["last_name"]
    assert response["email"] == payload["email"]
    assert participant["last_name"] == payload["last_name"]


def test_put_participant_with_invalid_data(auth_client):
    """Test try to edit participant with invalid email address."""
    payload = {"last_name": "TestTest", "email": "test"}
    rv = auth_client.post("/api/participants/", json=payload,)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert "Not a valid email address." in response["email"]


@pytest.mark.parametrize("method", ["get", "delete", "put"])
def test_get_delete_put_non_existing_participant(
    client, auth_client, add_participants, method
):
    """Test get, put and delete non-existing participant."""
    rv = getattr(auth_client, method)("/api/participants/11/")
    assert rv.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("method", ["get", "delete", "put"])
def test_get_delete_put_participant_unauthorized(client, add_participants, method):
    """Test get, put and delete participant with not logged in user."""
    rv = client.get("/api/participants/1/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


@pytest.mark.parametrize("field", ["email", "github"])
def test_try_edit_participant_with_existing_email_github(
    auth_client, add_participants, field
):
    """Test try to edit participant with other participant email address or github username."""
    all_participants = Participant.query.all()
    first_participant = all_participants[0]
    second_participant = all_participants[1]

    payload = {field: getattr(first_participant, field)}
    rv = auth_client.put(f"/api/participants/{second_participant.id}/", json=payload)
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.CONFLICT
    if field == "email":
        assert "User with this email already exists." in response["message"]
    else:
        assert "User with this Github login already exists." in response["message"]
