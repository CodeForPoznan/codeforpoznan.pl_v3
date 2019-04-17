import pytest

from backend.extensions import mail


def test_contact_us_endpoint(client, new_msg):
    """
    GIVEN an application instance, valid message, and mocked email outbox
    WHEN sending valid contact message to send-email endpoint
    THEN check status code, message, and email outbox
    """
    with mail.record_messages() as outbox:
        rv = client.post('/send-email/', json=new_msg)
        response = rv.get_json()

        assert rv.status == '200 OK'
        assert response["message"] == "Contact message successfully sent"
        assert len(outbox) == 1
        assert outbox[0].sender == "test@test.com"
        assert "Lorem Ipsum" in outbox[0].body


def test_contact_us_without_email(client, new_msg):
    """
    GIVEN an application instance and message without email
    WHEN sending invalid contact message to send-email endpoint
    THEN check if proper error was raised with 400 status code
    """
    del new_msg["email"]
    rv = client.post('/send-email/', json=new_msg)
    response = rv.get_json()

    assert rv.status == "400 BAD REQUEST"
    assert response["email"]["message"] == "Valid email is required"


def test_contact_us_without_content(client, new_msg):
    """
    GIVEN an application instance and message without content
    WHEN sending invalid contact message to send-email endpoint
    THEN check if proper error was raised with 400 status code
    """
    del new_msg["content"]
    rv = client.post('/send-email/', json=new_msg)
    response = rv.get_json()

    assert rv.status == "400 BAD REQUEST"
    assert response["content"]["message"] == "Content of message is required"
