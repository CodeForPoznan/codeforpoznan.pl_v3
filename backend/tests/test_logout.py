import pytest


def test_logout_user_with_valid_access_token(client, access_token):
    """
    GIVEN logged in user and app instance
    WHEN trying to logout with access token
    THEN check 200 status code and response
    """
    rv = client.delete('/auth/logout',
                       headers={'Authorization': 'Bearer {}'
                                .format(access_token)})
    response = rv.get_json()
    assert rv.status == '200 OK'
    assert response['msg'] == 'Successfully logged out'


def test_logout_user_without_token(client):
    """
    GIVEN an app instance
    WHEN trying to logout without access token
    THEN check if proper error was raised with 401 status code
    """
    rv = client.delete('/auth/logout')
    response = rv.get_json()
    assert rv.status == '401 UNAUTHORIZED'
    assert response['msg'] == 'Missing Authorization Header'
