from http import HTTPStatus

from flask import request
from flask_mail import Message
from flask_restful import Resource

from marshmallow import ValidationError

from backend.serializers.message_serializer import MessageSchema
from backend.extensions import mail


class SendMessage(Resource):
    def post(self):
        try:
            message_schema = MessageSchema()
            new_msg = message_schema.load(request.json)
        except ValidationError as err:
            return {"message": err.messages}, HTTPStatus.BAD_REQUEST
        msg = Message(
            subject="Email z cfp_v3 od {}".format(new_msg["name"]),
            sender=new_msg["email"],
            reply_to=new_msg["email"],
            recipients=["cfp@codeforpoznan.test"],
        )
        msg.body = f"Nowa wiadomość od {new_msg['name']}, \
            nr tel: {new_msg['phone']} \nTreść:\n {new_msg['content']}"
        mail.send(msg)

        return {"message": "Contact message successfully sent"}, HTTPStatus.OK
