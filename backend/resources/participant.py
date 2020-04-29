from http import HTTPStatus

from flask import request

from flask_jwt_extended import jwt_required
from flask_restful import Resource

from marshmallow import ValidationError

from backend.extensions import db
from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema


class ParticipantsList(Resource):
    @jwt_required
    def get(self):
        participant_schema = ParticipantSchema(many=True, exclude=("hacknights",))
        return (participant_schema.dump(Participant.query.all()), HTTPStatus.OK)

    @jwt_required
    def post(self):
        participant_schema = ParticipantSchema()
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, HTTPStatus.BAD_REQUEST
        try:
            data = participant_schema.load(json_data)
        except ValidationError as err:
            return (err.messages), HTTPStatus.BAD_REQUEST

        if Participant.query.filter_by(email=json_data["email"]).first():
            return (
                {"message": "User with this email already exists."},
                HTTPStatus.CONFLICT,
            )

        if Participant.query.filter_by(github=json_data["github"]).first():
            return (
                {"message": "User with this Github login already exists."},
                HTTPStatus.CONFLICT,
            )

        participant = Participant(**data)
        db.session.add(participant)
        db.session.commit()

        return participant_schema.dump(participant), HTTPStatus.CREATED


class ParticipantDetails(Resource):
    @jwt_required
    def get(self, id):
        participant_schema = ParticipantSchema()
        return participant_schema.dump(Participant.query.get_or_404(id)), HTTPStatus.OK

    @jwt_required
    def delete(self, id):
        participant = Participant.query.get_or_404(id)
        db.session.delete(participant)
        db.session.commit()

        return {"message": "Participant deleted successfully."}, HTTPStatus.OK

    @jwt_required
    def put(self, id):
        participant_schema = ParticipantSchema(partial=True)
        participant = Participant.query.get_or_404(id)
        json_data = request.get_json(force=True)
        try:
            data = participant_schema.load(json_data)
        except ValidationError as err:
            return err.messages, HTTPStatus.BAD_REQUEST

        for key, value in data.items():
            setattr(participant, key, value)
        db.session.add(participant)
        db.session.commit()
        return participant_schema.dump(participant), HTTPStatus.OK
