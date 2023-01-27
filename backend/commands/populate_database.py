import itertools
import random

import click
from flask.cli import with_appcontext
from tqdm import tqdm

from backend.extensions import db
from backend.factories import (
    HacknightFactory,
    ParticipantFactory,
    TeamFactory,
    TechStackFactory,
    UserFactory,
    UserSkillsFactory,
)
from backend.models import Participant, TechStack, User


@click.command()
@with_appcontext
def populate_database():
    """Populate database with fake data."""

    click.echo("Creating 5 users")
    usernames = []
    for _ in tqdm(range(5)):
        usernames.append(UserFactory.create().github_username)
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

    click.echo("Creating 10 tech_stacks")
    for _ in tqdm(range(10)):
        TechStackFactory.create()
        db.session.commit()

    click.echo("Creating 5 teams")
    all_techstacks = TechStack.query.all()
    for _ in tqdm(range(5)):
        TeamFactory.create(
            members=random.sample(all_participants, random.randint(1, 40)),
            tech_stack=random.sample(all_techstacks, random.randint(1, 10)),
        )
        db.session.commit()

    click.echo("Creating 10 skills linked to users")
    all_users = User.query.all()
    user_techstack_pairs = random.sample(
        set(itertools.product(all_users, all_techstacks)), 10
    )
    for pair in tqdm(user_techstack_pairs):
        UserSkillsFactory.create(user=pair[0], skill=pair[1])
        db.session.commit()

    click.echo("Created users:")
    for id, github_username in enumerate(usernames, start=1):
        click.echo(f"{id}. {github_username}")
