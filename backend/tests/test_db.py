import datetime
import pytest

from backend.models import User, Participant, Hacknight


def test_add_new_user_to_db(db_session, new_user):
    """
    GIVEN mocked db session, and user data
    WHEN a new user added to db
    THEN check the user data from db
    """
    assert len(db_session.query(User).all()) == 0

    new_user = User(username=new_user['username'],
                    password=new_user['password'])
    db_session.add(new_user)

    user = db_session.query(User).filter_by(username="TestName").first()

    assert user.username == "TestName"
    assert user.password == "TestPassword"


def test_add_new_participant_to_db(db_session, new_participant):
    """
    GIVEN mocked db session, and participant data
    WHEN a new participant added to db
    THEN check the participant data from db
    """
    assert len(db_session.query(Participant).all()) == 0

    new_participant = Participant(name=new_participant['name'],
                                  lastname=new_participant['lastname'],
                                  email=new_participant['email'],
                                  phone=new_participant['phone'])
    db_session.add(new_participant)

    participant = db_session.query(Participant).filter_by(name="Jon").first()

    assert participant.name == 'Jon'
    assert participant.lastname == 'Doe'
    assert participant.email == 'test@test.com'
    assert participant.phone == '123456789'


def test_add_new_hacknight_to_db(db_session, new_hacknight):
    """
    GIVEN mocked db session, and hacknight data
    WHEN a new hacknight added to db
    THEN check the hacknight data from db
    """
    assert len(db_session.query(Hacknight).all()) == 0

    new_hacknight = Hacknight(date=new_hacknight['date'])
    db_session.add(new_hacknight)

    hacknight = db_session.query(Hacknight).all()[0]

    assert hacknight.date == datetime.date(2000, 10, 10)
