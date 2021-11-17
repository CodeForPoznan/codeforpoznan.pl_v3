from http import HTTPStatus

import json

from backend.models import TechStack
from backend.serializers.techstack_serializer import TechStackSchema


def test_get_tech_stack_when_logged_in(auth_client, add_tech_stack):
    """Test get list of tech stacks for logged in user."""
    rv = auth_client.get("/api/techstacks/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert len(response) == 10


def test_get_tech_stack_with_empty_db(auth_client):
    """Test get list of tech stacks when no tech stack added to db."""
    rv = auth_client.get("/api/techstacks/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not response


def test_get_techstack_unauthorized(client, add_tech_stack):
    """Test get list of tech stacks when user is not logged in."""
    rv = client.get("/api/techstacks/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


def test_create_techstack_with_valid_data(
    auth_client, new_tech_stack,
):
    """Test add tech stack with valid data in payload."""
    techstack_schema = TechStackSchema()
    rv = auth_client.post("/api/techstacks/", data=json.dumps(new_tech_stack),)
    response = rv.get_json()
    techstack_db = TechStack.query.first()
    assert rv.status_code == HTTPStatus.CREATED
    assert response == techstack_schema.dump(techstack_db)


def test_try_create_techstack_without_payload(auth_client):
    """Test try to create new techstack without payload."""
    rv = auth_client.post("/api/techstacks/", json={})
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["message"] == "No input data provided"


def test_try_create_techstack_without_technology(auth_client, new_tech_stack):
    """Test try create new techstack without technology provided."""
    del new_tech_stack["technology"]

    rv = auth_client.post("/api/techstacks/", json=new_tech_stack)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST

    assert "Missing data for required field." in response["technology"]


def test_try_create_techstack_with_existing_technology(auth_client, new_tech_stack, _db):
    """Test try to create new techstack with existing technology."""
    db = _db
    techstack = TechStack(**new_tech_stack)
    db.session.add(techstack)
    db.session.commit()

    payload = {
        "technology": new_tech_stack["technology"],
        "label": "backend"
    }
    rv = auth_client.post("/api/techstacks/", json=payload)
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.CONFLICT
    assert "Tech stack with that technology already exists." in response["message"]
