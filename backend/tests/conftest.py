import datetime
import os
import tempfile

import pytest
from flask.testing import FlaskClient

from backend.app import create_app
from backend.extensions import db
from backend.factories import (
    HacknightFactory,
    ParticipantFactory,
    TeamFactory,
    TechStackFactory,
)
from backend.models import User


@pytest.fixture
def app():
    """Create and configure a new app instance for tests."""
    # create a temp file to isolate the db for each test
    db_fd, db_path = tempfile.mkstemp()
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DATABASE"] = db_path
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    # create the db and load test data
    with app.app_context():
        db.init_app(app)
        db.create_all()

    yield app

    # close and remove the temporary db
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def _db():
    """Create and configure a new db instance for pytest-flask-sqlalchemy."""
    db_fd, db_path = tempfile.mkstemp()
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DATABASE"] = db_path
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    with app.app_context():
        db.init_app(app)
        db.create_all()

        yield db

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def new_user():
    user = {
        "github_username": "TestName",
        "password": "TestPassword",
        "first_name": "Sheldon",
        "last_name": "Nowitzki",
        "email": "sheldon@nowitzki.test",
        "phone": "1234123",
        "slack": "mightysheldor",
        "is_admin": False,
    }
    return user


@pytest.fixture
def new_user_admin(new_user):
    user = new_user.copy()
    user["is_admin"] = True
    user["password"] = "TestPasswordAdmin"
    return user


@pytest.fixture
def new_participant():
    participant = {
        "first_name": "Jon",
        "last_name": "Doe",
        "email": "test@test.test",
        "phone": "123456789",
        "github_username": "wihajster",
        "slack": "slacklogin",
    }
    return participant


@pytest.fixture
def new_hacknight():
    hacknight = {"date": datetime.date(2000, 10, 10)}
    return hacknight


@pytest.fixture
def new_team():
    return {
        "project_name": "cfp_v3",
        "description": "Lorem Ipsum",
        "project_url": "https://www.cfp_v3.test",
    }


@pytest.fixture
def new_tech_stack():
    return {"technology": "Flask", "label": "backend"}


@pytest.fixture
def registered_user(new_user_admin, app, _db):
    new_user_admin = User(**new_user_admin)
    with app.app_context():
        db = _db
        db.session.add(new_user_admin)
        db.session.commit()
    return new_user_admin


@pytest.fixture
def tokens(app, client, new_user_admin, registered_user):
    with app.app_context():
        new_user_dict = {
            k: v
            for k, v in new_user_admin.items()
            if k == ("github_username") or k == ("password")
        }
        rv = client.post("/api/auth/login/", json=new_user_dict)
        response = rv.get_json()
        from backend.models import JWTToken

        print(len(JWTToken.query.all()))
        yield {"access": response["access_token"], "refresh": response["refresh_token"]}


@pytest.fixture
def auth_client(app, tokens):
    from backend.models import JWTToken

    print(len(JWTToken.query.all()))

    class CustomClient(FlaskClient):
        def open(self, *args, **kwargs):
            kwargs.setdefault("headers", []).append(
                ("Authorization", f"Bearer {tokens['access']}")
            )
            return super().open(*args, **kwargs)

    app.test_client_class = CustomClient
    return app.test_client()


@pytest.fixture
def new_msg():
    msg = {
        "name": "Happy Volunteer",
        "email": "hvolunteer@example.com",
        "phone": "777222333",
        "content": "I'm super excited to work with you guys!",
    }
    return msg


@pytest.fixture
def add_participants(app, _db):
    for _ in range(10):
        ParticipantFactory.create()
        _db.session.commit()


@pytest.fixture
def add_hacknights(app, _db):
    for _ in range(10):
        HacknightFactory.create()
        _db.session.commit()


@pytest.fixture
def add_participants_to_hacknight(app, _db):
    HacknightFactory(participants=ParticipantFactory.create_batch(10))
    _db.session.commit()


@pytest.fixture
def add_teams(app, _db):
    for _ in range(10):
        TeamFactory.create()
        _db.session.commit()


@pytest.fixture
def add_tech_stack(app, _db):
    for _ in range(10):
        TechStackFactory.create()
        _db.session.commit()


@pytest.fixture
def add_members_to_team(app, _db):
    TeamFactory(members=ParticipantFactory.create_batch(10))
    _db.session.commit()


@pytest.fixture
def add_techstack_to_team(app, _db):
    TeamFactory(tech_stack=TechStackFactory.create_batch(5))
    _db.session.commit()
