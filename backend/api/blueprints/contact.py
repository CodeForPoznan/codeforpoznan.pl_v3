from flask import Blueprint, jsonify, request
from flask_mail import Message
from flask_cors import CORS

from marshmallow import ValidationError

from api.serializers.message_serializer import message_schema
import api

contact = Blueprint('contact', __name__)
CORS(contact)  # enable CORS on the contact blue print


@contact.route('/send-email/', methods=['POST'])
def send_message():
    try:
        new_msg = message_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    msg = Message(
        subject='Email z cdf_v3 od {}'.format(new_msg["name"]),
        sender=new_msg["email"],
        reply_to=new_msg["email"],
        recipients=["cfp_v3@cfp_v3.com"]  # has to be change to valid email
    )
    msg.body = 'Nowa wiadomość od {}, nr tel: {} \nTreść:\n {}'.format(
        new_msg["name"],
        new_msg["phone"],
        new_msg["content"])
    api.mail.send(msg)

    return jsonify({"message": "Contact message successfully sent"}), 200
