from http import HTTPStatus
import json

from backend.models import Hacknight, Participant


def test_get_hacknights_when_logged_in(auth_client, add_hacknights):
    """Test get list of hacknights for logged in user."""
    rv = auth_client.get("/api/hacknights/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert len(response) == 10


def test_get_hacknights_with_empty_db(auth_client):
    """Test get list of hacknights when no hacknight added to db."""
    rv = auth_client.get("/api/hacknights/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not response


def test_get_hacknights_unauthorized(client, add_hacknights):
    """Test get list of hacknights when user is not logged in."""
    rv = client.get("/api/hacknights/")
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


def test_add_participants_to_hacknight(auth_client, add_hacknights, add_participants):
    """Test add new participant to hacknight."""
    payload = {"participants_ids": [1, 3]}
    rv = auth_client.post("/api/hacknights/1/participants/", data=json.dumps(payload),)
    resp = rv.get_json()
    assert rv.status_code == HTTPStatus.OK

    hacknight_db = Hacknight.query.get(1)
    ids_from_db = [participant.id for participant in hacknight_db.participants]
    for participant in resp["participants"]:
        assert participant["id"] in payload["participants_ids"]
    assert ids_from_db == payload["participants_ids"]


def test_add_participants_to_hacknight_unauthorized(
    add_hacknights, add_participants, client
):
    """Test add participants to hacknight when user is not logged in."""
    payload = {"participants_ids": [1, 3]}
    rv = client.post("/api/hacknights/1/participants/", data=json.dumps(payload))
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response["msg"] == "Missing Authorization Header"


def test_add_nonexisting_participants_to_hacknight(auth_client, add_hacknights):
    """Test add non-existing participants ids to hacknight."""
    payload = {"participants_ids": [1, 3]}
    rv = auth_client.post("/api/hacknights/1/participants/", data=json.dumps(payload),)
    assert rv.status_code == HTTPStatus.NOT_FOUND


def test_add_participants_to_nonexisting_hacknight(auth_client, add_participants):
    """Test add participants to non-existing hacknight."""
    payload = {"participants_ids": [1, 3]}
    rv = auth_client.post("/api/hacknights/1/participants/", data=json.dumps(payload),)
    assert rv.status_code == HTTPStatus.NOT_FOUND


def test_duplicate_participant_in_hacknight(
    auth_client, add_hacknights, add_participants, _db
):
    """Test add participant who is already in hacknight."""
    hacknight = _db.session.query(Hacknight).first()
    participant = _db.session.query(Participant).first()
    hacknight.participants.append(participant)

    payload = {"participants_ids": [participant.id]}
    rv = auth_client.post(
        f"/api/hacknights/{hacknight.id}/participants/", data=json.dumps(payload),
    )
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["message"] == "No new participant has been provided"


def test_create_hacknight_with_same_date(auth_client, new_hacknight, _db):
    """Test add hacknight with the same date."""
    db = _db
    new_hacknight = Hacknight(date=new_hacknight["date"])
    db.session.add(new_hacknight)
    db.session.commit()

    payload = {"date": "2000-10-10"}
    rv = auth_client.post("/api/hacknights/", data=json.dumps(payload),)
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.CONFLICT
    assert response["message"] == "Hacknight already exists."


def test_remove_participants_from_hacknight(auth_client, add_participants_to_hacknight):
    """Test remove single participant from hacknight."""
    hacknight_db = Hacknight.query.get(1)
    participant_id = hacknight_db.participants[0].id
    payload = {"participants_ids": [participant_id]}
    rv = auth_client.delete("/api/hacknights/1/participants/", data=json.dumps(payload))
    response = rv.get_json()
    participant_db = Participant.query.get(participant_id)
    assert rv.status_code == HTTPStatus.OK
    assert participant_db not in Hacknight.query.get(1).participants
    assert participant_db.id not in response.get("participants")


def test_remove_all_participants_from_hacknight(
    auth_client, add_participants_to_hacknight
):
    """Test remove all participants from hacknight."""
    hacknight_db = Hacknight.query.get(1)
    participants_id = [participant.id for participant in hacknight_db.participants]
    payload = {"participants_ids": participants_id}
    rv = auth_client.delete("/api/hacknights/1/participants/", data=json.dumps(payload))
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.OK
    assert not Hacknight.query.get(1).participants
    assert not response.get("participants")


def test_remove_wrong_participant_from_hacknight(
    auth_client, add_participants_to_hacknight
):
    """Test remove non-existing participant from hacknight."""
    payload = {"participants_ids": [999]}
    rv = auth_client.delete("/api/hacknights/1/participants/", data=json.dumps(payload))
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["message"] == "No participant to delete"
