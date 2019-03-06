import pytest


def test_login_with_valid_user(client, new_user, registered_user):
    """
    GIVEN registerd user and app instance
    WHEN login with valid user data
    THEN check if access token is in response
    """
    rv = client.post('/login', json={
                                     'username': new_user['username'],
                                     'password': new_user['password']
                                    })
    response = rv.get_json()
    assert rv.status == '200 OK'
    assert response['access_token']


def test_login_with_invalid_password(client, new_user, registered_user):
    """
    GIVEN registred user and app instance
    WHEN trying to login with wrong password
    THEN check if proper error was raised with 401 status code
    """
    rv = client.post('/login', json={
                                     'username': new_user['username'],
                                     'password': 'WrongPassword'
                                    })
    response = rv.get_json()
    assert rv.status == '401 UNAUTHORIZED'
    assert response['msg'] == 'Invalid credentials'


def test_login_with_invalid_name_password(client):
    """
    GIVEN an app instance and invalid user data
    WHEN trying to login with unregistered user
    THEN check if proper error was raised with 401 status code
    """
    rv = client.post('/login', json={
                                    'username': 'WronkName',
                                    'password': 'WrongPassword'
                                    })
    response = rv.get_json()
    assert rv.status == '401 UNAUTHORIZED'
    assert response['msg'] == 'Invalid credentials'
