import json
import os
import tempfile

import pytest

from api import create_app, db
from api.models import User, Participant, Hacknight


@pytest.fixture
def client():
    app = create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.init_app(app)

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


@pytest.fixture
def _db():
    app = create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.init_app(app)
        yield db


@pytest.fixture
def new_user():
    user = User(username='TestName', password='TestPassword')
    return user


@pytest.fixture
def new_participant():
    participant = Participant(
        name='Jon',
        lastname='Doe',
        email='test@test.com',
        phone='123456789'
    )
    return participant


@pytest.fixture
def new_hacknight():
    hacknight = Hacknight(date="1.1.2000")
    return hacknight


@pytest.fixture
def contact_message():
    message = {
        'name': 'testName',
        'email': 'test@email.com',
        'phone': '111111111',
        'content': "Lorem ipsum dolor sit amet"}
    return message
