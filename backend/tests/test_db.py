import datetime
import pytest

from backend.models import User, Participant, Hacknight


def test_add_new_user_to_db(_db, new_user):
    """Test adding user to DB with valid data."""

    db = _db
    assert len(db.session.query(User).all()) == 0
    new_user = User(
        username=new_user['username'],
        password=new_user['password']
    )
    db.session.add(new_user)
    db.session.commit()

    user = db.session.query(User).filter_by(username="TestName").first()

    assert user.username == "TestName"
    assert user.check_password('TestPassword')


def test_add_new_participant_to_db(_db, new_participant):
    """Test addind participant do DB with valid data."""

    db = _db
    assert len(db.session.query(Participant).all()) == 0

    new_participant = Participant(
        name=new_participant['name'],
        lastname=new_participant['lastname'],
        email=new_participant['email'],
        phone=new_participant['phone']
    )
    db.session.add(new_participant)
    db.session.commit()

    participant = db.session.query(Participant).filter_by(name="Jon").first()

    assert participant.name == 'Jon'
    assert participant.lastname == 'Doe'
    assert participant.email == 'test@test.com'
    assert participant.phone == '123456789'


def test_add_new_hacknight_to_db(_db, new_hacknight):
    """Test addind hacknight do DB with valid data."""
    db = _db
    assert len(db.session.query(Hacknight).all()) == 0

    new_hacknight = Hacknight(date=new_hacknight['date'])
    db.session.add(new_hacknight)
    db.session.commit()

    hacknight = db.session.query(Hacknight).all()[0]

    assert hacknight.date == datetime.date(2000, 10, 10)
