import random

import click
from flask.cli import with_appcontext
from tqdm import tqdm

from backend.extensions import db
from backend.factories import HacknightFactory, ParticipantFactory, UserFactory
from backend.models import Participant


@click.command()
@with_appcontext
def populate_database():
    """Populate database with fake data."""

    click.echo("Creating 5 users")
    usernames = []
    for _ in tqdm(range(5)):
        usernames.append(UserFactory.create().username)
        db.session.commit()

    click.echo("Creating 50 participants")
    for _ in tqdm(range(50)):
        ParticipantFactory.create()
        db.session.commit()

    click.echo("Creating 30 hacknights")
    all_participants = Participant.query.all()
    for _ in tqdm(range(30)):
        HacknightFactory.create(
            participants=random.sample(all_participants, random.randint(5, 30))
        )
        db.session.commit()

    click.echo("Created users:")
    for id, username in enumerate(usernames, start=1):
        click.echo(f"{id}. {username}")
