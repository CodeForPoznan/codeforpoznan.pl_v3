from http import HTTPStatus

from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema


def test_get_participant_when_logged_in(auth_client, add_participants):
    """Test get participant details for logged in user."""
    rv = auth_client.get("/participants/1/")
    response = rv.get_json()
    participant_schema = ParticipantSchema()
    assert rv.status_code == HTTPStatus.OK
    assert response == participant_schema.dump(Participant.query.get(1))


def test_get_non_existent_participant(auth_client, add_participants):
    """Test get detais of non-existent participant"""
    rv = auth_client.get("/participants/11/")
    assert rv.status_code == HTTPStatus.NOT_FOUND


def test_get_participant_unauthorized(client, add_participants):
    """Test get participant details for not logged in user."""
    rv = client.get("/participants/1/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"
