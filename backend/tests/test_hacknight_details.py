from http import HTTPStatus


def test_get_hacknight_details_authorized(
    client, access_token, add_participants_to_hacknight
):
    """Test get hacknight details for logged in user."""
    rv = client.get(
        '/hacknights/1/',
        headers={'Authorization': 'Bearer {}'.format(access_token)}
    )
    response = rv.get_json()

    assert rv.status_code == HTTPStatus.OK
    assert len(response['hacknights']['participants']) == 10


def test_no_hacknights_in_hacknights_participants(
    client, access_token, add_participants_to_hacknight
):
    """Test get hacknight details for logged in user."""
    rv = client.get(
        '/hacknights/1/',
        headers={'Authorization': 'Bearer {}'.format(access_token)}
    )
    response = rv.get_json()

    for participant in response['hacknights']['participants']:
        assert 'hacknights' not in participant
    assert rv.status_code == HTTPStatus.OK


def test_get_hacknight_details_unauthorized(
    client, add_participants_to_hacknight
):
    """Test get hacknight details for not logged in user."""
    rv = client.get('/participants/1/')
    response = rv.get_json()
    assert rv.status_code == HTTPStatus.UNAUTHORIZED
    assert response['msg'] == 'Missing Authorization Header'
