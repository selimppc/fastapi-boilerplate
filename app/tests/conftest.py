""" conftest """

import pytest_asyncio
from starlette.testclient import TestClient

from app.config import settings
from app.main import app
from app.mongodb import client as mongo_client


@pytest_asyncio.fixture(scope="session")
def test_client():
    """
    create client, db, and after test , db will ne deleted
    :return:
    """
    with TestClient(app) as test_client:
        yield test_client
        mongo_client.db.contents.drop()
    # delete_collections()


# @pytest.fixture
# async def async_test_client():
#     async with AsyncClient(app=app, base_url='http://test') as async_test_client:
#         yield async_test_client


def mock_decode_auth_token(token):
    """ mock func"""
    _ = token
    payload = {
        'username': '8801911111111',
        'platform_id': settings.TESTING_PLATFORM_ID,
        'client_id': 'c2228334-6c5a-4a01-b87f-2ae0e49edddf',
        'user_type': 'regular'
    }
    return payload
