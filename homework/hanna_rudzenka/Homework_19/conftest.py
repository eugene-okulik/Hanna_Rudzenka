import pytest
import requests
from test_api_with_pytest import base_url


@pytest.fixture(scope='session')
def start_end_testing_print():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def before_and_after_each_test_print():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def get_new_object_id():
    body = {
        "name": "Kate",
        "data": {
            "age": 30,
            "job": "doctor"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(base_url, json=body, headers=headers).json()
    object_id = response['id']
    yield object_id
    requests.delete(f'{base_url}/{object_id}')
