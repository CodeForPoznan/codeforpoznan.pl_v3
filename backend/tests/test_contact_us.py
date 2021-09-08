from http import HTTPStatus

from backend.extensions import mail


def test_contact_us_endpoint(client, new_msg):
    """Test sending valid message to send-email endpoint."""
    with mail.record_messages() as outbox:
        rv = client.post("/api/send-email/", json=new_msg)
        response = rv.get_json()

        assert rv.status_code == HTTPStatus.OK
        assert response["message"] == "Contact message successfully sent"

        assert len(outbox) == 2
        internal, external = outbox[0], outbox[1]

        assert "Email z" in internal.subject
        assert "I'm super excited" in internal.body
        assert internal.sender == "CodeForPoznan <notifications@localhost>"
        assert internal.reply_to == "CodeForPoznan <hello@localhost>"
        assert internal.recipients == ["CodeForPoznan <hello@localhost>"]

        assert "Witaj" in external.subject
        assert "Cześć" in external.body
        assert external.sender == "CodeForPoznan <notifications@localhost>"
        assert external.reply_to == "CodeForPoznan <hello@localhost>"
        assert external.recipients == ["Happy Volunteer <hvolunteer@example.com>"]


def test_contact_us_without_email(client, new_msg):
    """Test sending message with no email provided."""
    del new_msg["email"]
    rv = client.post("/api/send-email/", json=new_msg)
    response = rv.get_json()["message"]

    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["email"]["message"] == "Valid email is required"


def test_contact_us_without_content(client, new_msg):
    """Test sending message with no content provided."""
    del new_msg["content"]
    rv = client.post("/api/send-email/", json=new_msg)
    response = rv.get_json()["message"]

    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["content"]["message"] == "Content of message is required"
