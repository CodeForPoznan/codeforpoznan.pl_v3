from datetime import date, timedelta

from flask_jwt_extended import create_access_token

from backend.models import Hacknight, JWTToken, Participant, User
from backend.resources.auth import add_token_to_database


def test_add_new_user_to_db(_db, new_user):
    """Test adding user to DB with valid data."""

    db = _db
    assert len(db.session.query(User).all()) == 0
    new_user = User(**new_user)
    db.session.add(new_user)
    db.session.commit()

    user = db.session.query(User).filter_by(username="TestName").first()

    assert user.username == "TestName"
    assert user.check_password("TestPassword")


def test_add_new_participant_to_db(_db, new_participant):
    """Test addind participant do DB with valid data."""

    db = _db
    assert len(db.session.query(Participant).all()) == 0

    participant = Participant(**new_participant)
    db.session.add(participant)
    db.session.commit()

    participant_db = db.session.query(Participant).filter_by(first_name="Jon").first()

    for key, value in new_participant.items():
        assert getattr(participant_db, key) == value


def test_add_new_hacknight_to_db(_db, new_hacknight):
    """Test addind hacknight do DB with valid data."""
    db = _db
    assert len(db.session.query(Hacknight).all()) == 0

    new_hacknight = Hacknight(date=new_hacknight["date"])
    db.session.add(new_hacknight)
    db.session.commit()

    hacknight = db.session.query(Hacknight).first()

    assert hacknight.date == date(2000, 10, 10)


def test_remove_expired_token_method(_db):
    """Test remove_expired method for valid and expired tokens."""
    valid_token = create_access_token(identity=1)
    expired_token = create_access_token(
        identity=1, expires_delta=timedelta(microseconds=1)
    )
    add_token_to_database(valid_token)
    add_token_to_database(expired_token)
    tokens_db = _db.session.query(JWTToken).all()
    expired = [token.expired() for token in tokens_db]
    assert True in expired and False in expired

    JWTToken.remove_expired()
    assert len(_db.session.query(JWTToken).all()) == 1
