from http import HTTPStatus

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import Schema, ValidationError, fields

from backend.extensions import db
from backend.models import Hacknight, Participant
from backend.serializers.hacknight_serializer import HacknightSchema


class HacknightList(Resource):
    @jwt_required
    def get(self):
        hacknight_schema = HacknightSchema(many=True)
        return (
            hacknight_schema.dump(
                Hacknight.query.order_by(Hacknight.date.desc()).all()
            ),
            HTTPStatus.OK,
        )

    @jwt_required
    def post(self):
        hacknight_schema = HacknightSchema()
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, HTTPStatus.BAD_REQUEST
        try:
            data = hacknight_schema.load(json_data)
        except ValidationError as err:
            return (err.messages), HTTPStatus.BAD_REQUEST

        hacknight = Hacknight.query.filter_by(date=data["date"]).first()
        if hacknight:
            return {"message": "Hacknight already exists."}, HTTPStatus.CONFLICT
        hacknight = Hacknight(date=data["date"])
        db.session.add(hacknight)
        db.session.commit()

        return hacknight_schema.dump(hacknight), HTTPStatus.CREATED


class HacknightDetails(Resource):
    @jwt_required
    def get(self, id):
        hacknight_schema = HacknightSchema()

        return (
            {"hacknights": hacknight_schema.dump(Hacknight.query.get_or_404(id))},
            HTTPStatus.OK,
        )


class HacknightParticipants(Resource):
    @jwt_required
    def post(self, hacknight_id, participant_id):
        hacknight = Hacknight.query.get_or_404(hacknight_id)
        participants = [participant.id for participant in hacknight.participants]

        if participant_id in participants:
            return (
                {"message": "No new participant has been provided"},
                HTTPStatus.BAD_REQUEST,
            )

        hacknight.participants.append(Participant.query.get_or_404(participant_id))
        db.session.add(hacknight)
        db.session.commit()

        hacknight_schema = HacknightSchema()
        return hacknight_schema.dump(hacknight), HTTPStatus.OK

    @jwt_required
    def delete(self, hacknight_id, participant_id):
        hacknight = Hacknight.query.get_or_404(hacknight_id)
        existing_participants = {
            participant.id for participant in hacknight.participants
        }
        if participant_id not in existing_participants:
            return {"message": "No participant to delete"}, HTTPStatus.BAD_REQUEST
        hacknight.participants = [
            participant
            for participant in hacknight.participants
            if participant.id != participant_id
        ]
        db.session.commit()

        hacknight_schema = HacknightSchema()
        return hacknight_schema.dump(hacknight), HTTPStatus.OK
