import datetime

from backend.models import User, Participant, Hacknight


def test_create_new_user(new_user):
    """Test user model."""

    new_user = User(username=new_user["username"], password=new_user["password"])

    assert new_user.username == "TestName"
    assert new_user.check_password("TestPassword")


def test_create_new_participant(new_participant):
    """Test participant model."""
    new_participant = Participant(**new_participant)

    assert new_participant.first_name == "Jon"
    assert new_participant.last_name == "Doe"
    assert new_participant.email == "test@test.com"
    assert new_participant.phone == "123456789"


def test_create_new_hacknight(new_hacknight):
    """Test hacknight model."""

    new_hacknight = Hacknight(date=new_hacknight["date"])

    assert new_hacknight.date == datetime.date(2000, 10, 10)
