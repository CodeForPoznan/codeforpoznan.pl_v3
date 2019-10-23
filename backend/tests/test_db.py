import datetime
import pytest

from backend.models import User, Participant, Hacknight


def test_add_new_user_to_db(_db, new_user):
    """Test adding user to DB with valid data."""

    db = _db
    assert len(db.session.query(User).all()) == 0
    new_user = User(**new_user)
    db.session.add(new_user)
    db.session.commit()

    user = db.session.query(User).filter_by(username="TestName").first()

    assert user.username == "TestName"
    assert user.check_password('TestPassword')


def test_add_new_participant_to_db(_db, new_participant):
    """Test addind participant do DB with valid data."""

    db = _db
    assert len(db.session.query(Participant).all()) == 0

    participant = Participant(**new_participant)
    db.session.add(participant)
    db.session.commit()

    participant = db.session.query(Participant).filter_by(name="Jon").first()

    for key, value in new_participant.items():
        assert getattr(participant, key) == value


def test_add_new_hacknight_to_db(_db, new_hacknight):
    """Test addind hacknight do DB with valid data."""
    db = _db
    assert len(db.session.query(Hacknight).all()) == 0

    new_hacknight = Hacknight(date=new_hacknight['date'])
    db.session.add(new_hacknight)
    db.session.commit()

    hacknight = db.session.query(Hacknight).first()

    assert hacknight.date == datetime.date(2000, 10, 10)
