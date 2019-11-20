from http import HTTPStatus

from backend.extensions import mail


def test_contact_us_endpoint(client, new_msg):
    """Test sending valid message to send-email enndoint."""
    with mail.record_messages() as outbox:
        rv = client.post("/send-email/", json=new_msg)
        response = rv.get_json()

        assert rv.status_code == HTTPStatus.OK
        assert response["message"] == "Contact message successfully sent"
        assert len(outbox) == 1
        assert outbox[0].sender == "test@test.com"
        assert "Lorem Ipsum" in outbox[0].body


def test_contact_us_without_email(client, new_msg):
    """Test sending message with no email provided."""
    del new_msg["email"]
    rv = client.post("/send-email/", json=new_msg)
    response = rv.get_json()["message"]

    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["email"]["message"] == "Valid email is required"


def test_contact_us_without_content(client, new_msg):
    """Test sending message with no content provided."""
    del new_msg["content"]
    rv = client.post("/send-email/", json=new_msg)
    response = rv.get_json()["message"]

    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert response["content"]["message"] == "Content of message is required"
