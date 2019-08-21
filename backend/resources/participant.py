from http import HTTPStatus

from flask_jwt_extended import jwt_required
from flask_restful import Resource

from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema


class ParticipantsList(Resource):
    @jwt_required
    def get(self):
        participant_schema = ParticipantSchema(
            many=True, exclude=('hacknights',))
        return {"participants": participant_schema.dump(
            Participant.query.all())}, HTTPStatus.OK
