import pytest
from click.testing import CliRunner
from flask.cli import ScriptInfo

from backend.commands.populate_database import populate_database
from backend.models import Hacknight, Participant, User


@pytest.fixture
def script(app):
    return ScriptInfo(create_app=app)


def test_populate_database(app, _db, script):
    """Test populate_database command."""
    runner = CliRunner()
    result = runner.invoke(populate_database, obj=app)

    assert result.exit_code == 0
    assert "Creating 30 hacknights" in result.output
    assert len(Hacknight.query.all()) == 30
    assert "Creating 50 participants" in result.output
    assert len(Participant.query.all()) == 50
    assert "Creating 5 users" in result.output
    assert len(User.query.all()) == 5
    assert "Created users:" in result.output
