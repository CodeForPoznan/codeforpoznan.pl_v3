import pytest


def test_login_with_valid_user(client, new_user, registered_user):
    """Test logging with valid data."""
    rv = client.post(
        '/auth/login',
        json={'username': new_user['username'],
              'password': new_user['password']}
    )
    response = rv.get_json()
    assert rv.status == '201 CREATED'
    assert response['access_token']


def test_login_with_invalid_password(client, new_user, registered_user):
    """Test logging with invalid password."""
    rv = client.post(
        '/auth/login',
        json={'username': new_user['username'],
              'password': 'WrongPassword'}
    )
    response = rv.get_json()
    assert rv.status == '401 UNAUTHORIZED'
    assert response['msg'] == 'Not authorized'


def test_login_with_invalid_name_password(client):
    """Test logging with invalid name and password."""
    rv = client.post(
        '/auth/login',
        json={'username': 'WrongName',
              'password': 'WrongPassword'}
    )
    response = rv.get_json()
    assert rv.status == '401 UNAUTHORIZED'
    assert response['msg'] == 'Not authorized'
