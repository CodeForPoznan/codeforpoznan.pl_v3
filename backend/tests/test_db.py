from datetime import date, timedelta

from flask_jwt_extended import create_access_token

from backend.models import (
    Hacknight,
    JWTToken,
    Participant,
    Team,
    TechStack,
    User,
    UserSkill,
)
from backend.resources.auth import add_token_to_database


def test_add_new_user_to_db(_db, new_user):
    """Test adding user to DB with valid data."""

    db = _db
    assert len(db.session.query(User).all()) == 0
    new_user = User(**new_user)
    db.session.add(new_user)
    db.session.commit()

    user = db.session.query(User).filter_by(github_username="TestName").first()

    assert user.github_username == "TestName"
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


def test_add_new_team_to_db(_db, new_team):
    """Test adding team to DB with valid data."""
    db = _db
    assert len(db.session.query(Team).all()) == 0

    team = Team(**new_team)
    db.session.add(team)
    db.session.commit()

    team_db = db.session.query(Team).first()

    for key, value in new_team.items():
        assert getattr(team_db, key) == value


def test_add_new_tech_stach_to_db(_db, new_tech_stack):
    """Test adding tech stack to DB with valid data."""
    db = _db
    assert len(db.session.query(TechStack).all()) == 0

    tech_stack = TechStack(**new_tech_stack)
    db.session.add(tech_stack)

    tech_stack_db = db.session.query(TechStack).first()

    for key, value in new_tech_stack.items():
        assert getattr(tech_stack_db, key) == value


def test_add_new_skill_for_user(_db, new_user, new_tech_stack):
    """Test adding new skill for a user."""
    db = _db

    new_user = User(**new_user)
    tech_stack = TechStack(**new_tech_stack)
    db.session.add(tech_stack)
    db.session.add(new_user)
    db.session.commit()
    tech_stack_db = db.session.query(TechStack).first()
    user_db = db.session.query(User).first()

    user_skill = UserSkill(
        user_id=user_db.id, techstack_id=tech_stack_db.id, skill_level=2
    )
    db.session.add(user_skill)
    db.session.commit()

    user_skill_db = db.session.query(UserSkill).first()
    assert user_skill_db.user == user_db
    assert user_skill_db.skill == tech_stack_db
    assert user_skill_db.is_learning_goal == False
    assert user_skill_db.skill_level == 2


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
