from http import HTTPStatus

from flask import request

from flask_jwt_extended import jwt_required
from flask_restful import Resource

from marshmallow import fields, Schema, ValidationError

from backend.extensions import db
from backend.models import Hacknight, Participant
from backend.serializers.hacknight_serializer import HacknightSchema


class HacknightList(Resource):
    @jwt_required
    def get(self):
        hacknight_schema = HacknightSchema(many=True, exclude=("participants",))
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
    def post(self, id):
        hacknight = Hacknight.query.get_or_404(id)
        participants = [participant.id for participant in hacknight.participants]

        json_data = request.get_json(force=True)
        ids_schema = Schema.from_dict({"participants_ids": fields.List(fields.Int())})
        try:
            data = ids_schema().load(json_data)
        except ValidationError as err:
            return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY

        new_participants = [
            _id for _id in data["participants_ids"] if _id not in participants
        ]

        if not new_participants:
            return (
                {"message": "No new participant has been provided"},
                HTTPStatus.BAD_REQUEST,
            )

        for new_participant in new_participants:
            hacknight.participants.append(Participant.query.get_or_404(new_participant))
        db.session.add(hacknight)
        db.session.commit()

        hacknight_schema = HacknightSchema()
        return hacknight_schema.dump(hacknight), HTTPStatus.OK
