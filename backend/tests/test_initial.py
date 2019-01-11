import json
import os
import tempfile

import pytest

from api import create_app
from api.models import db


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




def test_empty_db(client):

    message = {
        'name': 'testName',
        'email': 'test@email.com',
        'phone': '111111111',
        'content': "Lorem ipsum dolor sit amet"}
    rv = client.post('/send-email/', json=message)
    json_data = rv.get_json()
    assert "Contact message successfully sent" in json_data['message']
