import time
from textwrap import dedent

from http import HTTPStatus

from flask import request, current_app
from flask_restful import Resource

from marshmallow import ValidationError

from backend.serializers.message_serializer import MessageSchema
from backend.extensions import mail
from backend.helpers import wrap_io


class MessageError(Exception):
    pass


class SendMessage(Resource):

    # available variables: name, email, phone, content, base_url

    internal_message_subject = """
        Email z {base_url} od {name}
    """

    internal_message_body = """
        Nowa wiadomość od {name} <{email}>
        numer telefonu: {phone}
        Treść:
        {content}
    """

    external_message_subject = """
        [Code fof Poznań] Witaj na pokładzie!
    """

    external_message_body = """
        Cześć,
        
        tu załoga Code For Poznań! Chcielibyśmy dać znać, że otrzymaliśmy Twoją wiadomość i postaramy się jak najszybciej na nią odpowiedzieć.
        
        Do usłyszenia wkrótce!
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.log = current_app.logger
        self.base_url = current_app.config["BASE_URL"]
        self.mail_web_server = current_app.config["MAIL_WEB_SERVER"]
        self.mail_suppress_send = current_app.config["MAIL_SUPPRESS_SEND"]

        self.hello_addr = f"hello@{self.base_url}"
        self.notify_addr = f"notifications@{self.base_url}"

    def post(self):
        try:
            message_schema = MessageSchema()
            data = message_schema.load(request.json)
        except ValidationError as err:
            return {"message": err.messages}, HTTPStatus.BAD_REQUEST

        sender_email = data["email"]
        context = {"base_url": self.base_url, **data}

        try:
            # mail from someone (via form) to us, send internal message
            self.send_message(
                context=context,
                subject=self.internal_message_subject,
                body=self.internal_message_body,
                sender=self.notify_addr,
                reply_to=self.notify_addr,
                recipients=[self.hello_addr],
            )

            # mail from us to someone, send pretty external message
            self.send_message(
                context=context,
                subject=self.external_message_subject,
                body=self.external_message_body,
                sender=self.notify_addr,
                reply_to=self.hello_addr,
                recipients=[sender_email],
            )

        except MessageError:
            return (
                {"message": "Failed to send contact message"},
                HTTPStatus.SERVICE_UNAVAILABLE,
            )

        return {"message": "Contact message successfully sent"}, HTTPStatus.OK

    def send_message(self, *, context: dict, subject: str, body: str, **kwargs):
        subject = dedent(subject).format(**context).strip()
        body = dedent(body).format(**context).strip()

        with wrap_io() as (out, err):
            time.sleep(0.2)  # conservative throttle of 200ms/req for API
            mail.send_message(subject=subject, body=body, **kwargs)

        # skip error checking if we don't interact with server at all
        if self.mail_suppress_send:
            return

        stderr = err()

        if "MSGID=" not in stderr:
            self.log.error("Failed to send mail: stderr:\n", stderr)
            raise MessageError(stderr)

        # bit rough, but works okay-ish
        msgid = stderr.split("MSGID=")[1].split("]")[0]
        link = self.mail_web_server + msgid
        self.log.info(f"Mail sent successfully! {link}")
