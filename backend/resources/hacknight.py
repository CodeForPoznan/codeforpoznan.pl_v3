from backend.extensions import db

from http import HTTPStatus

from flask import request

from flask_jwt_extended import jwt_required
from flask_restful import Resource

from marshmallow import ValidationError

from backend.models import Hacknight

from backend.serializers.hacknight_serializer import hacknight_schema, hacknights_schema


class HacknightList(Resource):
    @jwt_required
    def get(self):
        hacknight_list = Hacknight.query.all()
        if hacknight_list:
            hacknights = hacknights_schema.dump(hacknight_list)
            return {"hacknights": hacknights}, HTTPStatus.OK
        return {"message": "Hacknight not found"}, HTTPStatus.NOT_FOUND

    @jwt_required
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, HTTPStatus.BAD_REQUEST
        try:
            data = hacknight_schema.load(json_data)
        except ValidationError as err:
            return (err.messages), HTTPStatus.BAD_REQUEST

        hacknight = Hacknight.query.filter_by(date=data['date']).first()
        if hacknight:
            return ({'message': 'Hacknight already exists.'}), HTTPStatus.BAD_REQUEST
        hacknight = Hacknight(
            date=data['date'],
        )
        db.session.add(hacknight)
        db.session.commit()

        return ({'message': 'Hacknight created successfully.'}), HTTPStatus.CREATED
