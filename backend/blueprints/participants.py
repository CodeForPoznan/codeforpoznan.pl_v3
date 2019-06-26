from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from backend.models import Participant
from backend.serializers.participant_serializer import (
    participant_schema, participants_schema
)

participants = Blueprint('participants', __name__)


@participants.route('/participant/<int:id>', methods=['GET'])
@jwt_required
def get_participant(id):
    participant = Participant.find_by_id(id)

    if participant:
        return jsonify(participant_schema.dump(participant)), 200
    return jsonify({"message": "Participant not found"}), 404


@participants.route('/participants', methods=['GET'])
@jwt_required
def get_participants_list():
    participants_list = Participant.query.all()
    if participants_list:
        participants = participants_schema.dump(participants_list)
        return jsonify({"participants": participants}), 200
    return jsonify({"message": "participants not found"}), 404
