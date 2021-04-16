import logging
from textwrap import dedent

from http import HTTPStatus

from flask import request
from flask import current_app
from flask_restful import Resource

from marshmallow import ValidationError

from backend.serializers.message_serializer import MessageSchema
from backend.extensions import mail
from backend.helpers import wrap_io


MAIL_RECIPIENT = current_app.config["MAIL_RECIPIENT"]
MAIL_WEB_SERVER = current_app.config["MAIL_WEB_SERVER"]
BASE_URL = current_app.config["BASE_URL"]


class SendMessage(Resource):
    def post(self):
        try:
            message_schema = MessageSchema()
            data = message_schema.load(request.json)
        except ValidationError as err:
            return {"message": err.messages}, HTTPStatus.BAD_REQUEST

        name, email = data["name"], data["email"]
        phone, content = data["phone"], data["content"]

        subject = f"""
            Email z {BASE_URL} od {name}
        """

        body = f"""
            Nowa wiadomość od {name}
            numer telefonu: {phone}
            Treść:
            {content}
        """

        status_code = self._send_message(
            sender=email,
            reply_to=email,
            recipients=[MAIL_RECIPIENT],
            subject=dedent(subject).strip(),
            body=dedent(body).strip(),
        )

        if status_code == HTTPStatus.OK:
            return {"message": "Contact message successfully sent"}, status_code
        else:
            return {"message": "Failed to send contact message"}, status_code

    @staticmethod
    def _send_message(**kwargs):
        with wrap_io() as (out, err):
            mail.send_message(**kwargs)

        # known mail testing domain, find message link in output
        if MAIL_WEB_SERVER:
            if "MSGID=" in err():
                msgid = err().split("MSGID=")[1].split("]")[0]
                link = f"https://ethereal.email/message/{msgid}"
                logging.info(f"Mail sent successfully: {link}")
                return HTTPStatus.OK
            else:
                logging.error("Failed to send mail, SMTP stderr:\n", err())
                return HTTPStatus.SERVICE_UNAVAILABLE

        # real smtp server
        else:
            # TODO: parse SES SMTP server responses like we already do above
            logging.info(f"Mail sent: stdout:\n", out(), "\n stderr:\n", err())
            return HTTPStatus.OK
