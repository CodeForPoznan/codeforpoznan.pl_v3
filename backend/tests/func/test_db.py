import pytest

from api import db
from api.models import User, Participant, Hacknight


def test_add_new_user_to_db(db_session, new_user):
    """
    GIVEN mocked db session, and user instance
    WHEN a new user added to db
    THEN check the user data from db
    """
    db.create_all()
    assert len(db_session.query(User).all()) == 0

    db_session.add(new_user)
    db_session.commit()
    row = db_session.query(User).all()
    assert len(row) == 1
    assert row[0].username == "TestName"
    assert row[0].password == "TestPassword"


def test_add_new_participant_to_db(db_session, new_participant):
    """
    GIVEN mocked db session, and participant instance
    WHEN a new participant added to db
    THEN check the participant data from db
    """
    db.create_all()
    assert len(db_session.query(Participant).all()) == 0

    db_session.add(new_participant)
    db_session.commit()
    row = db_session.query(Participant).all()
    assert len(row) == 1
    assert row[0] == new_participant


def test_add_new_hacknight_to_db(db_session, new_hacknight):
    """
    GIVEN mocked db session, and hacknight instance
    WHEN a new hacknight added to db
    THEN check the hacknight data from db
    """
    db.create_all()
    assert len(db_session.query(Hacknight).all()) == 0

    db_session.add(new_hacknight)
    db_session.commit()
    row = db_session.query(Hacknight).all()
    assert len(row) == 1
    assert row[0].date == "1.1.2000"
