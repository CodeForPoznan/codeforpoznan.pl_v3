import csv
import click

from flask.cli import with_appcontext
from backend.models import Hacknight
from backend.extensions import db


@click.command()
@with_appcontext
def import_attendance_list():
    """Import attendance list."""
    rows = []
    list_of_users = []
    users_dict = {}

    # open file from exported csv
    with open("./temp/list.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            rows.append(row)

    # get dates of historical hacknights
    dates = rows[0][4:]
    click.echo(f"Created list of dates: {dates}")

    # skip header
    rows = rows[1:]
    # prepare users' data
    for item in rows:
        _id, github, name, phone, email, *values = item
        try:
            first_name = name.split()[0]
        except:
            pass
        try:
            last_name = name.split()[1]
        except:
            pass

        users_dict["id"] = _id
        users_dict["github"] = github
        users_dict["first_name"] = first_name
        users_dict["last_name"] = last_name
        users_dict["email"] = email
        users_dict["phone"] = phone

        list_of_users.append(users_dict)
        users_dict = {}

    # create hacknights
    for date in dates:
        splitted_date = date.split(".")
        formatted_date = f"{splitted_date[2]}-{splitted_date[1]}-{splitted_date[0]}"
        hacknight = Hacknight(date=formatted_date)
        db.session.add(hacknight)
    db.session.commit()
    click.echo(f"Imported {len(dates)} hacknights")
