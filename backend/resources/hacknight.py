from http import HTTPStatus

from flask_jwt_extended import jwt_required
from flask_restful import Resource

from backend.models import Hacknight
from backend.serializers.hacknight_serializer import HacknightSchema


class HacknightList(Resource):
    @jwt_required
    def get(self):
        hacknight_schema = HacknightSchema(
            many=True, exclude=('participants',))
        return {'hacknights': hacknight_schema.dump(
            Hacknight.query.all())}, HTTPStatus.OK
