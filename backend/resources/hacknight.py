from http import HTTPStatus

from flask import request

from flask_jwt_extended import jwt_required
from flask_restful import Resource

from marshmallow import ValidationError

from backend.extensions import db
from backend.models import Hacknight
from backend.serializers.hacknight_serializer import HacknightSchema


class HacknightList(Resource):
    @jwt_required
    def get(self):
        hacknight_schema = HacknightSchema(
            many=True, exclude=('participants',))
        return {'hacknights': hacknight_schema.dump(
            Hacknight.query.all())}, HTTPStatus.OK

    @jwt_required
    def post(self):
        hacknight_schema = HacknightSchema()
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, \
                HTTPStatus.BAD_REQUEST
        try:
            data = hacknight_schema.load(json_data)
        except ValidationError as err:
            return (err.messages), HTTPStatus.BAD_REQUEST

        hacknight = Hacknight.query.filter_by(date=data['date']).first()
        if hacknight:
            return {'message': 'Hacknight already exists.'}, \
                HTTPStatus.CONFLICT
        hacknight = Hacknight(
            date=data['date'],
        )
        db.session.add(hacknight)
        db.session.commit()

        return {'message': 'Hacknight created successfully.',
                "hacknight": data}, HTTPStatus.CREATED


class HacknightDetails(Resource):
    @jwt_required
    def get(self, id):
        hacknight_schema = HacknightSchema()

        return {'hacknights': hacknight_schema.dump(Hacknight.query.get_or_404(
            id))
        }, HTTPStatus.OK
