def test_send_valid_message(client, contact_message):
    """
    GIVEN test client and valid message
    WHEN sending valid message
    THEN check success response
    """
    rv = client.post('/send-email/', json=contact_message)
    response = rv.get_json()
    assert 'Contact message successfully sent' in response['message']
    assert rv.status == '200 OK'


def test_send_msg_without_name(client, contact_message):
    """
    GIVEN test client and massage without name
    WHEN sending invalid message
    THEN check if proper validation error for name was raised
    """
    contact_message.pop('name')
    rv = client.post('/send-email/', json=contact_message)
    response = rv.get_json()
    assert "Missing data for required field." in response['name']
    assert rv.status == '400 BAD REQUEST'


def test_send_msg_with_invalid_email(client, contact_message):
    """
    GIVEN test client and massage with invalid email, and without any
    WHEN sending invalid message
    THEN check if proper validation errors for email was raised
    """
    contact_message['email'] = 'invalid_email'
    rv = client.post('/send-email/', json=contact_message)
    response = rv.get_json()
    assert "Not a valid email address." in response['email']
    assert rv.status == '400 BAD REQUEST'

    contact_message.pop('email')
    rv = client.post('/send-email/', json=contact_message)
    response = rv.get_json()
    assert "Valid email is required" in response['email']['message']
    assert rv.status == '400 BAD REQUEST'
