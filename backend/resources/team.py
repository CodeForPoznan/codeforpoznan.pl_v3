from http import HTTPStatus

from flask import request

from flask_jwt_extended import jwt_required
from flask_restful import Resource

from marshmallow import fields, Schema, ValidationError

from backend.extensions import db
from backend.models import Participant, Team
from backend.serializers.team_serializer import TeamSchema


class TeamList(Resource):
    @jwt_required
    def get(self):
        team_schema = TeamSchema(many=True, exclude=("members",))
        return (
            team_schema.dump(Team.query.all()),
            HTTPStatus.OK,
        )

    @jwt_required
    def post(self):
        team_schema = TeamSchema()
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, HTTPStatus.BAD_REQUEST
        try:
            data = team_schema.load(json_data)
        except ValidationError as err:
            return (err.messages), HTTPStatus.BAD_REQUEST

        if Team.query.filter_by(project_name=data["project_name"]).first():
            return (
                {"message": "Team with that project_name already exists."},
                HTTPStatus.CONFLICT,
            )
        if Team.query.filter_by(project_url=data["project_url"]).first():
            return (
                {"message": "Team with that project_url already exists."},
                HTTPStatus.CONFLICT,
            )
        team = Team(**data)
        db.session.add(team)
        db.session.commit()

        return team_schema.dump(team), HTTPStatus.CREATED


class TeamDetails(Resource):
    @jwt_required
    def get(self, id):
        team_schema = TeamSchema()
        return team_schema.dump(Team.query.get_or_404(id)), HTTPStatus.OK

    @jwt_required
    def delete(self, id):
        team = Team.query.get_or_404(id)
        db.session.delete(team)
        db.session.commit()
        return HTTPStatus.OK

    @jwt_required
    def put(self, id):
        team_schema = TeamSchema(partial=True)
        team = Team.query.get_or_404(id)
        json_data = request.get_json(force=True)
        try:
            data = team_schema.load(json_data)
        except ValidationError as err:
            return err.messages, HTTPStatus.BAD_REQUEST

        for key, value in data.items():
            setattr(team, key, value)
        db.session.add(team)
        db.session.commit()
        return team_schema.dump(team), HTTPStatus.OK


class TeamMembers(Resource):
    @jwt_required
    def post(self, id):
        team = Team.query.get_or_404(id)
        members = [member.id for member in team.members]

        json_data = request.get_json(force=True)
        ids_schema = Schema.from_dict({"members_ids": fields.List(fields.Int())})
        try:
            data = ids_schema().load(json_data)
        except ValidationError as err:
            return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY

        new_members = [_id for _id in data["members_ids"] if _id not in members]
        if not new_members:
            return (
                {"message": "No new member has been provided"},
                HTTPStatus.BAD_REQUEST,
            )

        for new_member in new_members:
            team.members.append(Participant.query.get_or_404(new_member))
        db.session.add(team)
        db.session.commit()

        team_schema = TeamSchema()
        return team_schema.dump(team), HTTPStatus.OK

    @jwt_required
    def delete(self, id):
        team = Team.query.get_or_404(id)
        members = {member.id for member in team.members}

        json_data = request.get_json(force=True)
        ids_schema = Schema.from_dict({"members_ids": fields.List(fields.Int())})
        try:
            data = ids_schema().load(json_data)
        except ValidationError as err:
            return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY

        to_remove = members.intersection(set(data["members_ids"]))
        if not to_remove:
            return {"message": "No member to delete"}, HTTPStatus.BAD_REQUEST

        team.members = [member for member in team.members if member.id not in to_remove]
        db.session.commit()
        team_schema = TeamSchema()
        return team_schema.dump(team), HTTPStatus.OK
