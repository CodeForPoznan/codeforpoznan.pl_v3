from datetime import datetime, timedelta
from http import HTTPStatus

from backend.extensions import db
from backend.models import User, JWTToken
from backend.serializers.login_serializer import LoginSchema
from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    decode_token,
    get_jwt_identity,
    jwt_refresh_token_required,
    jwt_required,
    jwt_optional,
    get_raw_jwt,
)
from flask_restful import Resource
from marshmallow import ValidationError


class UserLogin(Resource):
    @jwt_optional
    def post(self):
        current_user = get_jwt_identity()

        if current_user:
            return (
                {"msg": f"User already logged in as {current_user}"},
                HTTPStatus.UNAUTHORIZED,
            )

        if not request.is_json:
            return {"msg": "No input data provided"}, HTTPStatus.BAD_REQUEST

        schema = LoginSchema()
        try:
            result = schema.load(request.json)
        except ValidationError as error:
            return (
                {"msg": "Wrong input data", "errors": error.messages},
                HTTPStatus.BAD_REQUEST,
            )

        username = result["username"]
        password = result["password"]

        if not (username and password):
            return ({"msg": "Username and password required"}, HTTPStatus.BAD_REQUEST)

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            access_token = create_access_token(
                identity=username, expires_delta=timedelta(minutes=60)
            )

            refresh_token = create_refresh_token(
                identity=username, expires_delta=timedelta(weeks=1)
            )

            ret = {"access_token": access_token, "refresh_token": refresh_token}

            add_token_to_database(access_token)
            add_token_to_database(refresh_token)
            return ret, HTTPStatus.CREATED
        else:
            return {"msg": "Not authorized"}, HTTPStatus.UNAUTHORIZED


class UserLogout(Resource):
    @jwt_required
    def delete(self):
        jti = get_raw_jwt()["jti"]
        token = JWTToken.query.filter_by(jti=jti).one()
        token.revoked = True
        db.session.commit()
        return {"msg": "Successfully logged out"}, HTTPStatus.OK


class RefreshAccessToken(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()

        access_token = create_access_token(
            identity=current_user, expires_delta=timedelta(minutes=60)
        )
        add_token_to_database(access_token)

        return {"access_token": access_token}, HTTPStatus.CREATED


class RefreshToken(Resource):
    @jwt_refresh_token_required
    def delete(self):
        jti = get_raw_jwt()["jti"]
        token = JWTToken.query.filter_by(jti=jti).one()
        token.revoked = True
        db.session.commit()
        return {"msg": "Refresh token successfully revoked"}, HTTPStatus.OK


def add_token_to_database(encoded_token):
    """
    Adds a new token to the database. It is not revoked when it is added.
    :param identity_claim:
    """
    decoded_token = decode_token(encoded_token)
    jti = decoded_token["jti"]
    token_type = decoded_token["type"]
    user_identity = decoded_token["identity"]
    expires = datetime.fromtimestamp(decoded_token["exp"])
    revoked = False

    db_token = JWTToken(
        jti=jti,
        token_type=token_type,
        user_identity=user_identity,
        expires=expires,
        revoked=revoked,
    )
    db.session.add(db_token)
    db.session.commit()
