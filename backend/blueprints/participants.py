from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from backend.models import Participant
from backend.serializers.participant_serializer import participants_schema

participants = Blueprint('participants', __name__)


@participants.route('/participants', methods=['GET'])
@jwt_required
def get_participants_list():
    participants_list = Participant.query.all()
    if participants_list:
        participants = participants_schema.dump(participants_list)
        return jsonify({"participants": participants}), 200
    return jsonify({"message": "participants not found"}), 404
