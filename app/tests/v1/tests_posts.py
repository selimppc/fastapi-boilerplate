""" test content """

from app.tests.conftest import mock_decode_auth_token


def test_content_details(test_client, monkeypatch):
    """
    Test get all department api
    """
    monkeypatch.setattr("app.security.decode_auth_token", mock_decode_auth_token)
    payload = {
        'id': 'c2228334-6c5a-4a01-b87f-2ae0e49edddf',
        'platform_id': 'db0a00dd-004c-4eed-ae18-3837ed43538a',
        'title': {
            'en': 'encanto test',
            'bn': None
        },
        'content_type': 'VOD',
        'genre': [
            'animation',
            'drama'
        ],
        'system_id': 'AbcD1234zxc'
    }
    response = test_client.post('/api/v1/contents',
                                json=payload,
                                headers={'Authorization': 'Bearer token'})
    print(response)
    response = test_client.get('/api/v1/contents/c2228334-6c5a-4a01-b87f-2ae0e49edddf')

    print(response.json())

# def test_department_create_api_success(client, get_jwt_token):
#     """Test api create department"""
#     url = url_for('user-management.department_department_list_api')
#     token = f'Bearer {get_jwt_token(permissions=[*PermissionList.DEPARTMENT_CREATE])}'
#
#     department_data = {
#         'name': 'rnd'
#     }
#     response = client.post(
#         url,
#         headers={'Authorization': token},
#         json=department_data
#     )
#
#     assert response.status_code == 201
#     assert response.json['name'] == 'rnd'
