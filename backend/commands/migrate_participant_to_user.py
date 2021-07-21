import click

from flask.cli import with_appcontext
from backend.models import Participant, User
from backend.extensions import db


@click.command()
@with_appcontext
def migrate_participant_to_user():
    """Migrate participant model instances into user model instances."""

    list_of_participants = []

    # prepare users' data
    for participant in Participant.query.all():
        users_dict = {"is_admin": False, "password": ""}

        users_dict["github_username"] = participant.github_username
        users_dict["first_name"] = participant.first_name
        users_dict["last_name"] = participant.last_name
        users_dict["email"] = participant.email
        users_dict["phone"] = participant.phone
        users_dict["slack"] = participant.slack

        list_of_participants.append(users_dict)

    # create users
    for participant in list_of_participants:
        new_user = User(**participant)
        db.session.add(new_user)
    db.session.commit()

    click.echo(f"Migrated {len(list_of_participants)} users")

    db.session.commit()
