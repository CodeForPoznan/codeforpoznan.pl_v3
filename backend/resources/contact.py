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
        name, phone, content = new_msg["name"], new_msg["phone"], new_msg["content"]
        msg = Message(
            subject=f"Email z cfp_v3 od {name}",
            sender=new_msg["email"],
            reply_to=new_msg["email"],
            recipients=["cfp@codeforpoznan.test"],
        )
        msg.body = f"Nowa wiadomość od {name}, nr tel: {phone} \nTreść:\n {content}"
        mail.send(msg)

        return {"message": "Contact message successfully sent"}, HTTPStatus.OK
