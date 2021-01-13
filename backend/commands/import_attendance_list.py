import csv
import click

from flask.cli import with_appcontext
from backend.models import Hacknight, Participant
from backend.extensions import db


@click.command()
@with_appcontext
def import_attendance_list():
    """Import attendance list."""
    rows = []
    list_of_participants = []
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
        first_name = name.split()[0]
        last_name = name.split()[1]

        users_dict["id"] = _id
        users_dict["github"] = github
        users_dict["first_name"] = first_name
        users_dict["last_name"] = last_name
        users_dict["email"] = email
        users_dict["phone"] = phone

        list_of_participants.append(users_dict)
        users_dict = {}

    # create hacknights
    for date in dates:
        splitted_date = date.split(".")
        formatted_date = f"{splitted_date[2]}-{splitted_date[1]}-{splitted_date[0]}"
        hacknight = Hacknight(date=formatted_date)
        db.session.add(hacknight)
    db.session.commit()
    click.echo(f"Imported {len(dates)} hacknights")

    # create participants
    for idx, participant in enumerate(list_of_participants):
        if participant["email"] == "":
            participant["email"] = f"unkown_email_{idx}"
        if participant["github"] == "":
            participant["github"] = f"unkown_github_{idx}"
        new_participant = Participant(
            id=participant["id"],
            github=participant["github"],
            first_name=participant["first_name"],
            last_name=participant["last_name"],
            email=participant["email"],
            phone=participant["phone"],
        )
        db.session.add(new_participant)
    db.session.commit()
    click.echo(f"Imported {len(list_of_participants)} participants")

    # assign attendance list
    for idx, row in enumerate(rows, 1):
        for index, element in enumerate(row[5:], 1):
            participant = Participant.query.get(idx)
            if element == "1":
                hacknight = Hacknight.query.get(index)
                hacknight.participants.append(participant)
                db.session.commit()
                click.echo(f"Added {participant.github} to hacknight {hacknight.date}")
