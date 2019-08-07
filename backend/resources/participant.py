from backend.extensions import db

from http import HTTPStatus

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from backend.models import Participant
from backend.serializers.participant_serializer import *

from marshmallow import ValidationError


class ParticipantsList(Resource):
    @jwt_required
    def get(self):
        participant_schema = ParticipantSchema(
            many=True, exclude=('hacknights',))
        return {"participants": participant_schema.dump(
            Participant.query.all())}, HTTPStatus.OK

    @jwt_required
    def post(self):
        participant_schema = ParticipantSchema()
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
            name=data['name'],
            lastname=data['lastname'],
            email=data['email'],
            github=data['github'],
            phone=data['phone']
        )
        db.session.add(participant)
        db.session.commit()

        return ({"message": "Participant created successfully."}), \
            HTTPStatus.CREATED
