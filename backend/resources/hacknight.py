from http import HTTPStatus

from flask_jwt_extended import jwt_required
from flask_restful import Resource

from backend.models import Hacknight
from backend.serializers.hacknight_serializer import hacknights_schema


class HacknightList(Resource):
    @jwt_required
    def get(self):
        hacknights = hacknights_schema.dump(Hacknight.query.all())
        return {'hacknights': hacknights}, HTTPStatus.OK
