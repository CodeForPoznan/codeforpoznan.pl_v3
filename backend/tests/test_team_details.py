from http import HTTPStatus
import json

import pytest

from backend.models import Participant, Team
from backend.serializers.team_serializer import TeamSchema


def test_get_team_when_logged_in(auth_client, add_teams):
    """Test get team details when logged in."""
    team_db = Team.query.first()
    rv = auth_client.get(f"/api/teams/{team_db.id}/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert response == TeamSchema().dump(team_db)


def test_delete_team_when_logged_in(app, auth_client, add_teams):
    """Test delete team details when logged in."""
    rv = auth_client.delete(f"/api/teams/1/")
    assert rv.status_code == HTTPStatus.OK
    assert not Team.query.get(1)


def test_edit_team_data_when_logged_in(app, auth_client, add_teams):
    """Test edit team details for logged in user and valid data."""
    with app.app_context():
        payload = {"project_name": "New Project", "description": "Another description"}
        rv = auth_client.put("/api/teams/1/", json=payload,)
        response = rv.get_json()
        schema = TeamSchema()
        team = schema.dump(Team.query.first())
    assert rv.status_code == HTTPStatus.OK
    for key, value in payload.items():
        assert team.get(key) == value
        assert response.get(key) == value


@pytest.mark.parametrize("method", ["get", "delete", "put"])
def test_get_delete_put_non_existing_team(auth_client, add_teams, method):
    """Test get, put and delete non-existing team."""
    rv = getattr(auth_client, method)("/api/teams/11/")
    assert rv.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("method", ["get", "delete", "put"])
def test_get_delete_put_team_unauthorized(client, add_teams, method):
    """Test get, put and delete team with not logged in user."""
    rv = getattr(client, method)("/api/teams/1/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


def test_add_members_to_team(auth_client, add_teams, add_participants):
    """Test add new members to a team."""
    payload = {"members_ids": [1, 3]}
    rv = auth_client.post("/api/teams/1/members/", data=json.dumps(payload),)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK

    team_db = Team.query.get(1)
    ids_from_db = [member.id for member in team_db.members]
    for member in response["members"]:
        assert member["id"] in payload["members_ids"]
    assert ids_from_db == payload["members_ids"]


def test_add_members_to_team_unauthorized(add_teams, add_participants, client):
    """Test add members to team when user is not logged in."""
    payload = {"members_ids": [1, 3]}
    rv = client.post("/api/teams/1/members/", data=json.dumps(payload))
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


def test_add_nonexisting_members_to_team(auth_client, add_teams):
    """Test add non-existing members ids to team."""
    payload = {"members_ids": [1, 3]}
    rv = auth_client.post("/api/teams/1/members/", data=json.dumps(payload),)
    assert rv.status_code == HTTPStatus.NOT_FOUND


def test_add_members_to_nonexisting_team(auth_client, add_participants):
    """Test add members to non-existing team."""
    payload = {"members_ids": [1, 3]}
    rv = auth_client.post("/api/teams/1/members/", data=json.dumps(payload),)
    assert rv.status_code == HTTPStatus.NOT_FOUND


def test_duplicate_member_in_team(auth_client, add_teams, add_participants, _db):
    """Test add member who is already in team."""
    team = _db.session.query(Team).first()
    member = _db.session.query(Participant).first()
    team.members.append(member)

    payload = {"members_ids": [member.id]}
    rv = auth_client.post(f"/api/teams/{team.id}/members/", data=json.dumps(payload),)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["message"] == "No new member has been provided"


def test_remove_member_from_team(auth_client, add_members_to_team):
    """Test remove single member from team."""
    team_db = Team.query.get(1)
    member_id = team_db.members[0].id
    payload = {"members_ids": [member_id]}
    rv = auth_client.delete("/api/teams/1/members/", data=json.dumps(payload))
    response = rv.get_json()
    member_db = Participant.query.get(member_id)
    assert rv.status_code == HTTPStatus.OK
    assert member_db not in Team.query.get(1).members
    assert member_db.id not in response.get("members")


def test_remove_all_members_from_team(auth_client, add_members_to_team):
    """Test remove all members from team."""
    team_db = Team.query.get(1)
    member_ids = [member.id for member in team_db.members]
    payload = {"members_ids": member_ids}
    rv = auth_client.delete("/api/teams/1/members/", data=json.dumps(payload))
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not Team.query.get(1).members
    assert not response.get("members")
