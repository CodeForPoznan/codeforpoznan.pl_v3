import datetime

from backend.models import User, Participant, Hacknight


def test_create_new_user(new_user):
    """Test user model."""

    new_user = User(username=new_user["username"], password=new_user["password"])

    assert new_user.username == "TestName"
    assert new_user.check_password("TestPassword")


def test_create_new_participant(new_participant):
    """Test participant model."""
    participant = Participant(**new_participant)

    for key, value in new_participant.items():
        assert getattr(participant, key) == value


def test_create_new_hacknight(new_hacknight):
    """Test hacknight model."""

    new_hacknight = Hacknight(date=new_hacknight["date"])

    assert new_hacknight.date == datetime.date(2000, 10, 10)
