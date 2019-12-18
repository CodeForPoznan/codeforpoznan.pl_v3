from http import HTTPStatus

import pytest

from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema


@pytest.mark.parametrize("method", ["get", "delete"])
def test_get_delete_participant_when_logged_in(
    client, access_token, add_participants, method
):
    """Test get and delete participant details for logged in user."""
    rv = getattr(client, method)(
        "/participants/1/", headers={"Authorization": "Bearer {}".format(access_token)}
    )
    response = rv.get_json()
    participant_schema = ParticipantSchema()
    assert rv.status_code == HTTPStatus.OK
    if method == "get":
        assert response == participant_schema.dump(Participant.query.get(1))
    else:
        assert response["message"] == "Participant deleted successfully."


@pytest.mark.parametrize("method", ["get", "delete", "put"])
def test_get_delete_put_non_existing_participant(
    client, access_token, add_participants, method
):
    """Test get and delete non-existing participant."""
    rv = getattr(client, method)(
        "/participants/11/", headers={"Authorization": "Bearer {}".format(access_token)}
    )
    assert rv.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("method", ["get", "delete", "put"])
def test_get_delete_put_participant_unauthorized(client, add_participants, method):
    """Test get and delete participant with not logged in user."""
    rv = client.get("/participants/1/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"
