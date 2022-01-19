from http import HTTPStatus

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from marshmallow import ValidationError

from backend.extensions import db
from backend.models import TechStack
from backend.serializers.techstack_serializer import TechStackSchema


class TechStackList(Resource):
    @jwt_required
    def get(self):
        techstack_schema = TechStackSchema(many=True, exclude=("teams",))
        return (
            techstack_schema.dump(TechStack.query.all()),
            HTTPStatus.OK,
        )

    @jwt_required
    def post(self):
        techstack_schema = TechStackSchema()
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, HTTPStatus.BAD_REQUEST
        try:
            data = techstack_schema.load(json_data)
        except ValidationError as err:
            return (err.messages), HTTPStatus.BAD_REQUEST

        if TechStack.query.filter_by(technology=data["technology"]).first():
            return (
                {"message": "Tech stack with that technology already exists."},
                HTTPStatus.CONFLICT,
            )

        techstack = TechStack(**data)
        db.session.add(techstack)
        db.session.commit()

        return techstack_schema.dump(techstack), HTTPStatus.CREATED


class TechStackDetails(Resource):
    @jwt_required
    def get(self, id):
        techstack_schema = TechStackSchema()
        return techstack_schema.dump(TechStack.query.get_or_404(id)), HTTPStatus.OK

    @jwt_required
    def delete(self, id):
        techstack = TechStack.query.get_or_404(id)
        db.session.delete(techstack)
        db.session.commit()
        return HTTPStatus.OK

    @jwt_required
    def put(self, id):
        techstack_schema = TechStackSchema(partial=True)
        techstack = TechStack.query.get_or_404(id)
        json_data = request.get_json(force=True)
        try:
            data = techstack_schema.load(json_data)
        except ValidationError as err:
            return err.messages, HTTPStatus.BAD_REQUEST

        for key, value in data.items():
            setattr(techstack, key, value)
        db.session.add(techstack)
        db.session.commit()
        return techstack_schema.dump(techstack), HTTPStatus.OK
