from http import HTTPStatus
import json

import pytest

from backend.models import TechStack
from backend.serializers.techstack_serializer import TechStackSchema


def test_get_techstack_when_logged_in(auth_client, add_tech_stack):
    """Test get tech stack details when logged in."""
    techstack_db = TechStack.query.first()
    rv = auth_client.get(f"/api/techstacks/{techstack_db.id}/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert response == TechStackSchema().dump(techstack_db)


def test_delete_team_when_logged_in(app, auth_client, add_tech_stack):
    """Test delete tech stack details when logged in."""
    rv = auth_client.delete(f"/api/techstacks/1/")
    assert rv.status_code == HTTPStatus.OK
    assert not TechStack.query.get(1)


def test_edit_techstack_data_when_logged_in(app, auth_client, add_tech_stack):
    """Test edit techstack details for logged in user and valid data."""
    with app.app_context():
        payload = {"technology": "Vue", "label": "frontend"}
        rv = auth_client.put("/api/techstacks/1/", json=payload,)
        response = rv.get_json()
        schema = TechStackSchema()
        techstack = schema.dump(TechStack.query.first())
    assert rv.status_code == HTTPStatus.OK
    for key, value in payload.items():
        assert techstack.get(key) == value
        assert response.get(key) == value


@pytest.mark.parametrize("method", ["get", "delete", "put"])
def test_get_delete_put_non_existing_techstack(auth_client, add_tech_stack, method):
    """Test get, put and delete non-existing tech stack."""
    rv = getattr(auth_client, method)("/api/techstacks/11/")
    assert rv.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("method", ["get", "delete", "put"])
def test_get_delete_put_techstack_unauthorized(client, add_tech_stack, method):
    """Test get, put and delete techstack with not logged in user."""
    rv = getattr(client, method)("/api/techstacks/1/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"
