import logging
from textwrap import dedent

from http import HTTPStatus

from flask import request, current_app
from flask_restful import Resource

from marshmallow import ValidationError

from backend.serializers.message_serializer import MessageSchema
from backend.extensions import mail
from backend.helpers import wrap_io


class SendMessage(Resource):

    internal_message_subject = """
    """

    internal_message_body = """
    """

    external_message_subject = """
        Email z {base_url} od {name}
    """

    external_message_body = """
        Nowa wiadomość od {name}
        numer telefonu: {phone}
        Treść:
        {content}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base_url = current_app.config["BASE_URL"]
        self.mail_recipient = current_app.config["MAIL_RECIPIENT"]
        self.mail_web_server = current_app.config["MAIL_WEB_SERVER"]

    def post(self):
        try:
            message_schema = MessageSchema()
            data = message_schema.load(request.json)
        except ValidationError as err:
            return {"message": err.messages}, HTTPStatus.BAD_REQUEST

        sender_email = data["email"]
        context = {
            **data,
            'base_url': self.base_url,
            'mail_recipient': self.mail_recipient,
        }

        try:
            # outgoing mail from someone (via form) to us, send internal message
            self.send_message(
                subject=self.internal_message_subject,
                body=self.internal_message_body,
                context=context,
                sender=sender_email,
                reply_to=sender_email,
                recipients=[self.mail_recipient],
            )

            # outgoing mail from us to someone, send pretty external message
            self.send_message(
                subject=self.external_message_subject,
                body=self.external_message_body,
                context=context,
                sender=self.mail_recipient,
                reply_to=self.mail_recipient,
                recipients=[sender_email],
            )
        except:
            return {"message": "Contact message successfully sent"}, HTTPStatus.OK

        return {"message": "Failed to send contact message"}, HTTPStatus.SERVICE_UNAVAILABLE

    def send_message(self, *, subject: str, body: str, context: dict, **kwargs):
        subject = dedent(subject).strip().format(**context)
        body = dedent(body).strip().format(**context)

        with wrap_io() as (out, err):
            mail.send_message(subject=subject, body=body, **kwargs)

        # known mail testing domain, find message link in output
        if self.mail_web_server:
            if "MSGID=" in err():
                msgid = err().split("MSGID=")[1].split("]")[0]
                link = f"https://ethereal.email/message/{msgid}"
                logging.info(f"Mail sent successfully: {link}")
            else:
                logging.error("Failed to send mail, SMTP stderr:\n", err())
                # TODO: raise 503
                # TODO: fix logging
                return HTTPStatus.SERVICE_UNAVAILABLE

        # real smtp server
        else:
            # TODO: parse SES SMTP server responses like we already do above
            logging.info(f"Mail sent: stdout:\n", out(), "\n stderr:\n", err())
            return HTTPStatus.OK
