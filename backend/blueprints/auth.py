from datetime import datetime, timedelta

from backend.extensions import db
from backend.models import User, JWTToken
from backend.serializers.login_serializer import LoginSchema
from flask import Blueprint, current_app as app, jsonify, request
from flask_jwt_extended import (
    create_access_token, create_refresh_token, decode_token,
    get_jwt_identity, jwt_required, jwt_optional, get_raw_jwt
)
from marshmallow import ValidationError


auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@auth_blueprint.route('/login', methods=['POST'])
@jwt_optional
def login():
    current_user = get_jwt_identity()

    if current_user:
        return jsonify({"msg": "User already logged in as {}".format(
            current_user)}), 401

    if not request.is_json:
        return jsonify({"msg": "No input data provided"}), 400

    schema = LoginSchema()
    try:
        result = schema.load(request.json)
    except ValidationError as error:
        return jsonify({"msg": "Wrong input data",
                        "errors": error.messages}), 400

    username = result['username']
    password = result['password']

    if not (username and password):
        return jsonify({"msg": "Username and password required"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(
            identity=username, expires_delta=timedelta(minutes=60))
        refresh_token = create_refresh_token(
            identity=username)

        add_token_to_database(access_token, app.config['JWT_IDENTITY_CLAIM'])
        add_token_to_database(refresh_token, app.config['JWT_IDENTITY_CLAIM'])

        ret = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        return jsonify(ret), 201
    else:
        return jsonify({"msg": "Not authorized"}), 401


@auth_blueprint.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    token = JWTToken.query.filter_by(jti=jti).one()
    token.revoked = True
    db.session.commit()
    return jsonify({"msg": "Successfully logged out"}), 200


def add_token_to_database(encoded_token, identity_claim):
    """
    Adds a new token to the database. It is not revoked when it is added.
    :param identity_claim:
    """
    decoded_token = decode_token(encoded_token)
    jti = decoded_token['jti']
    token_type = decoded_token['type']
    user_identity = decoded_token[identity_claim]
    expires = datetime.fromtimestamp(decoded_token['exp'])
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


def is_token_revoked(decoded_token):
    """
    Checks if the given token is revoked or not. Because we are adding all the
    tokens that we create into this database, if the token is not present
    in the database we are going to consider it revoked, as we don't know where
    it was created.
    """
    jti = decoded_token['jti']
    try:
        token = JWTToken.query.filter_by(jti=jti).one()
        return token.revoked
    except NoResultFound:
        return True
