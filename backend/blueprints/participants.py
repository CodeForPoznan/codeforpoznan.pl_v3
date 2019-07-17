from backend.extensions import db

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from backend.models import Participant
from backend.serializers.participant_serializer import ParticipantSchema

from marshmallow import ValidationError

participants = Blueprint('participants', __name__)


@participants.route('/participants', methods=['GET'])
@jwt_required
def get_participants_list():
    participants_list = Participant.query.all()
    if participants_list:
        participants = ParticipantSchema.dump(participants_list)
        return jsonify({"participants": participants}), 200
    return jsonify({"message": "participants not found"}), 404


@participants.route('/participants', methods=['POST'])
@jwt_required
def create_praticipant():
    json_data = request.get_json(force=True)
    if not json_data:
        return {'message': 'No input data provided'}, 400

    schema = ParticipantSchema()
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    participant = Participant.query.filter_by(name=data['name']).first()
    if participant:
        return jsonify({"message": "Participant already exists."}), 400
    participant = Participant(
        name=json_data['name'],
        lastname=json_data['lastname'],
        email=json_data['email'],
        github=json_data['github'],
        phone=json_data['phone']
    )
    db.session.add(participant)
    db.session.commit()
    # result = ParticipantSchema.dump(participant).data

    return jsonify({"message": "Participant created successfully."}), 201
