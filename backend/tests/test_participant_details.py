from http import HTTPStatus

import pytest

from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema


@pytest.mark.parametrize("method", ["get", "delete"])
def test_get_delete_participant_when_logged_in(
    client, auth_client, add_participants, method
):
    """Test get and delete participant details for logged in user."""
    rv = getattr(auth_client, method)("/participants/1/")
    response = rv.get_json()
    participant_schema = ParticipantSchema()
    assert rv.status_code == HTTPStatus.OK
    if method == "get":
        assert response == participant_schema.dump(Participant.query.get(1))
    else:
        assert response["message"] == "Participant deleted successfully."


@pytest.mark.parametrize("method", ["get", "delete"])
def test_get_delete_non_existing_participant(
    client, auth_client, add_participants, method
):
    """Test get and delete non-existing participant."""
    rv = getattr(auth_client, method)("/participants/11/")
    assert rv.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("method", ["get", "delete"])
def test_get_delete_participant_unauthorized(client, add_participants, method):
    """Test get and delete participant with not logged in user."""
    rv = client.get("/participants/1/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"
