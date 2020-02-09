from datetime import timedelta

import pytest
from click.testing import CliRunner
from flask.cli import ScriptInfo
from flask_jwt_extended import create_access_token

from backend.commands.remove_expired_tokens import remove_expired_tokens
from backend.commands.populate_database import populate_database
from backend.models import Hacknight, JWTToken, Participant, User
from backend.resources.auth import add_token_to_database


@pytest.fixture
def script(app):
    return ScriptInfo(create_app=lambda info: app)


def test_populate_database(script):
    """Test populate_database command."""
    runner = CliRunner()
    result = runner.invoke(populate_database, obj=script)
    app = script._loaded_app
    assert result.exit_code == 0
    assert "Creating 30 hacknights" in result.output
    assert "Creating 50 participants" in result.output
    assert "Creating 5 users" in result.output
    assert "Created users:" in result.output
    with app.app_context():
        assert len(Hacknight.query.all()) == 30
        assert len(Participant.query.all()) == 50
        assert len(User.query.all()) == 5


def test_remove_expired_tokens(script):
    """Test removing tokens from database command."""
    runner = CliRunner()
    runner.invoke(remove_expired_tokens, obj=script)
    app = script._loaded_app

    with app.app_context():
        add_token_to_database(create_access_token(identity=1))
        for _ in range(5):
            add_token_to_database(
                create_access_token(identity=1, expires_delta=timedelta(microseconds=1))
            )
        assert len(JWTToken.query.all()) == 6

    result = runner.invoke(remove_expired_tokens, obj=script)
    assert result.exit_code == 0
    assert "Removing expired tokens" in result.output
    assert "Done!" in result.output
    with app.app_context():
        assert len(JWTToken.query.all()) == 1
