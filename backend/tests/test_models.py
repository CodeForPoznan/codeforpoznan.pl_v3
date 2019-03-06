import datetime
import pytest

from backend.models import User, Participant, Hacknight


def test_create_new_user(new_user):
    """
    GIVEN a User data
    WHEN a new User is created
    THEN check the username and password
    """
    new_user = User(username=new_user['username'],
                    password=new_user['password'])

    assert new_user.username == 'TestName'
    assert new_user.check_password('TestPassword')


def test_create_new_participant(new_participant):
    """
    GIVEN a Participant data
    WHEN a new Participant is created
    THEN check the fullname, email and phone
    """
    new_participant = Participant(name=new_participant['name'],
                                  lastname=new_participant['lastname'],
                                  email=new_participant['email'],
                                  phone=new_participant['phone'])

    assert new_participant.name == 'Jon'
    assert new_participant.lastname == 'Doe'
    assert new_participant.email == 'test@test.com'
    assert new_participant.phone == '123456789'


def test_create_new_hacknight(new_hacknight):
    """
    GIVEN a Hacknight data
    WHEN a new Hacknight is created
    THEN check the hacknight date
    """
    new_hacknight = Hacknight(date=new_hacknight['date'])

    assert new_hacknight.date == datetime.date(2000, 10, 10)
