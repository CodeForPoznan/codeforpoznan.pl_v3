import click
from flask.cli import with_appcontext

from backend.models import JWTToken


@click.command()
@with_appcontext
def remove_expired_tokens():
    """Remove expired tokens from database."""
    click.echo("Removing expired tokens")
    JWTToken.remove_expired()
    click.echo("Done!")
