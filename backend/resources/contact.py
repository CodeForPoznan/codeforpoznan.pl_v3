from http import HTTPStatus

from flask import request
from flask_mail import Message
from flask_restful import Resource

from marshmallow import ValidationError

from backend.serializers.message_serializer import message_schema
from backend.extensions import mail


class SendMessage(Resource):
    def post(self):
        try:
            new_msg = message_schema.load(request.json)
        except ValidationError as err:
            return {"message": err.messages}, HTTPStatus.BAD_REQUEST
        msg = Message(
            subject='Email z cfp_v3 od {}'.format(new_msg["name"]),
            sender=new_msg["email"],
            reply_to=new_msg["email"],
            recipients=["cfp@codeforpoznan.test"]
        )
        msg.body = 'Nowa wiadomość od {}, nr tel: {} \nTreść:\n {}'.format(
            new_msg["name"],
            new_msg["phone"],
            new_msg["content"])
        mail.send(msg)

        return {"message": "Contact message successfully sent"}, HTTPStatus.OK
