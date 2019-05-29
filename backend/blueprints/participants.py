from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from backend.models import Participant


participants = Blueprint('participants', __name__)

@participants.route('participants', methods=['GET'])
@jwt_required
def get_participants_list():
    participants_list = Participant.query.all()
    return participants_list




