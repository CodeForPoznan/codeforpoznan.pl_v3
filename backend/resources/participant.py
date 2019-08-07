from backend.extensions import db

from http import HTTPStatus

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from backend.models import Participant
from backend.serializers.participant_serializer import (
    participants_schema, participant_schema
)

from marshmallow import ValidationError


class ParticipantsList(Resource):
    @jwt_required
    def get(self):
        return {"participants": participants_schema.dump(
            Participant.query.all())}, HTTPStatus.OK

    @jwt_required
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, \
                HTTPStatus.BAD_REQUEST
        try:
            data = participant_schema.load(json_data)
        except ValidationError as err:
            return (err.messages), HTTPStatus.BAD_REQUEST

        participant = Participant.query.filter_by(name=data['name']).first()
        if participant:
            return ({'message': 'Participant already exists.'}), \
                HTTPStatus.BAD_REQUEST
        participant = Participant(
            name=json_data['name'],
            lastname=json_data['lastname'],
            email=json_data['email'],
            github=json_data['github'],
            phone=json_data['phone']
        )
        db.session.add(participant)
        db.session.commit()

        return ({"message": "Participant created successfully."}), \
            HTTPStatus.CREATED
