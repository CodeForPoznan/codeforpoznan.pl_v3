import re
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
        [CfP] Email z {base_url} od {name}
    """

    internal_message_body = """
        Nowa wiadomość od {name} <{email}>
        numer telefonu: {phone}
        Treść:
        
        {content}
    """

    external_message_subject = """
        [Code for Poznań] Witaj na pokładzie!
    """

    external_message_body = """
        Cześć,
        
        Chcielibyśmy dać znać, że otrzymaliśmy Twoją wiadomość i postaramy się jak najszybciej na nią odpowiedzieć.
        
        Pozdrawiamy,
        załoga Code for Poznań
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.log = current_app.logger
        self.base_url = current_app.config["BASE_URL"]
        self.mail_web_url = current_app.config["MAIL_WEB_URL"]
        self.mail_suppress_send = current_app.config["MAIL_SUPPRESS_SEND"]

        self.hello_addr = f"CodeForPoznan <hello@{self.base_url}>"
        self.notify_addr = f"CodeForPoznan <notifications@{self.base_url}>"

    def post(self):
        try:
            message_schema = MessageSchema()
            data = message_schema.load(request.json)
        except ValidationError as err:
            return {"message": err.messages}, HTTPStatus.BAD_REQUEST

        sender_name, sender_email = data["name"], data["email"]
        sender_email = f"{sender_name} <{sender_email}>"
        context = {"base_url": self.base_url, **data}

        try:
            # mail from someone (via form) to us, send internal message
            self.send_message(
                context=context,
                subject=self.internal_message_subject,
                body=self.internal_message_body,
                sender=self.notify_addr,
                reply_to=self.hello_addr,
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

        with wrap_io() as (_, err):
            time.sleep(0.2)  # conservative throttle of 200ms/req for API
            mail.send_message(subject=subject, body=body, **kwargs)

        # skip error checking if we don't interact with server at all
        if self.mail_suppress_send:
            return

        stderr = err()

        # example successful responses from ethereal and ses, respectively:
        # data: (250, b'Accepted [STATUS=new MSGID=YRbuVPOb3gQndRMOYRubW3BtxAZI8iBfAAAAAbdiFY1fwZ4LCwdvaNWoIDs]')
        # data: (250, b'Ok 0102017b4c5776db-6639a4be-4c46-469b-b528-edf2b28e686a-000000')

        if resp := re.search(r"data: \(250, b'(.*)'", stderr):
            msg = resp.groups()[0]
            msg = re.search(r"[\w+.-]{10,}", msg).group(0)
            link = self.mail_web_url + msg
            self.log.info(f"Mail sent successfully! {link}")
        else:
            self.log.error("Failed to send mail: stderr:\n", stderr)
            raise MessageError(stderr)
