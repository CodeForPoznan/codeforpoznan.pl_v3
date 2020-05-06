import os
import datetime
import tempfile

from flask.testing import FlaskClient
import pytest

from backend.app import create_app
from backend.extensions import db
from backend.factories import HacknightFactory, ParticipantFactory
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
    user = {"username": "TestName", "password": "TestPassword"}
    return user


@pytest.fixture
def new_participant():
    participant = {
        "first_name": "Jon",
        "last_name": "Doe",
        "email": "test@test.com",
        "phone": "123456789",
        "github": "wihajster",
        "slack": "slacklogin",
    }
    return participant


@pytest.fixture
def new_hacknight():
    hacknight = {"date": datetime.date(2000, 10, 10)}
    return hacknight


@pytest.fixture
def registered_user(new_user, app, _db):
    new_user = User(**new_user)
    with app.app_context():
        db = _db
        db.session.add(new_user)
        db.session.commit()
    return new_user


@pytest.fixture
def tokens(app, client, new_user, registered_user):
    with app.app_context():
        rv = client.post("/auth/login/", json=new_user)
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
        "name": "TestName",
        "email": "test@test.com",
        "phone": "777222333",
        "content": "Lorem Ipsum cos tam cos tam",
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
