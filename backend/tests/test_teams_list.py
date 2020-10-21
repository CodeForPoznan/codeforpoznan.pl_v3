from http import HTTPStatus

import json

from backend.models import Team
from backend.serializers.team_serializer import TeamSchema


def test_get_teams_when_logged_in(auth_client, add_teams):
    """Test get list of teams for logged in user."""
    rv = auth_client.get("/api/teams/")
    response = rv.get_json()
    print(response)
    assert rv.status_code == HTTPStatus.OK
    assert len(response) == 10


def test_get_teams_with_empty_db(auth_client):
    """Test get list of teams when no team added to db."""
    rv = auth_client.get("/api/hacknights/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not response


def test_get_teams_unauthorized(client, add_teams):
    """Test get list of hacknights when user is not logged in."""
    rv = client.get("/api/hacknights/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


def test_create_team_with_valid_data(
    auth_client, new_team,
):
    """Test add team with valid data in payload."""
    team_schema = TeamSchema()
    rv = auth_client.post("/api/teams/", data=json.dumps(new_team),)
    response = rv.get_json()
    team_db = Team.query.first()
    assert rv.status_code == HTTPStatus.CREATED
    assert response == team_schema.dump(team_db)


def test_try_create_team_without_payload(auth_client):
    """Test try to create new team without payload."""
    rv = auth_client.post("/api/teams/", json={})
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["message"] == "No input data provided"


def test_try_create_team_without_project_name(auth_client, new_team):
    """Test try create new participant without project_name."""
    del new_team["project_name"]

    rv = auth_client.post("/api/teams/", json=new_team)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST

    assert "Missing data for required field." in response["project_name"]


def test_try_create_team_with_existing_project_name(auth_client, new_team, _db):
    """Test try to create new team with existing project_name."""
    db = _db
    team = Team(**new_team)
    db.session.add(team)
    db.session.commit()

    payload = {
        "project_name": new_team["project_name"],
        "description": "Lorem Ipsum Test",
        "project_url": "https://www.cfp_v4.test",
    }
    rv = auth_client.post("/api/teams/", json=payload)
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.CONFLICT
    assert "Team with that project_name already exists." in response["message"]


def test_try_create_team_with_existing_project_url(auth_client, new_team, _db):
    """Test try to create new team with existing project_name."""
    db = _db
    team = Team(**new_team)
    db.session.add(team)
    db.session.commit()

    payload = {
        "project_name": "New Team",
        "description": "Lorem Ipsum Test",
        "project_url": new_team["project_url"],
    }
    rv = auth_client.post("/api/teams/", json=payload)
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.CONFLICT
    assert "Team with that project_url already exists." in response["message"]
