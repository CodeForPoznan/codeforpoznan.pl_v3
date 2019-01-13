import pytest

from api.models import User, Participant, Hacknight


def test_create_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username and password
    """
    assert new_user.username == 'TestName'
    assert new_user.password == 'TestPassword'


def test_create_new_participant(new_participant):
    """
    GIVEN a Participant model
    WHEN a new Participant is created
    THEN check the fullname, email and phone
    """
    assert new_participant.name == 'Jon'
    assert new_participant.lastname == 'Doe'
    assert new_participant.email == 'test@test.com'
    assert new_participant.phone == '123456789'


def test_create_new_hacknight(new_hacknight):
    """
    GIVEN a Hacknight model
    WHEN a new Hacknight is created
    THEN check the hacknight date
    """
    assert new_hacknight.date == "1.1.2000"
