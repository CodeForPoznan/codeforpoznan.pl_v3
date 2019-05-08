import click
from flask.cli import with_appcontext

from backend.extensions import db
from backend.factories import HacknightFactory, ParticipantFactory, UserFactory


@click.command()
@with_appcontext
def populate_database():
    """Populate database with fake data."""

    for _ in range(3):
        UserFactory.create()

    for _ in range(15):
        HacknightFactory.create()

    for _ in range(50):
        ParticipantFactory.create()

    db.session.commit()
