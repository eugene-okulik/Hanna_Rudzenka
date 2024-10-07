import pytest
import requests

base_url = 'http://167.172.172.115:52353/object'


@pytest.fixture(scope='session')
def start_end_testing_print():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def before_each_test_print():
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


@pytest.mark.critical
@pytest.mark.parametrize('body', [
    {"name": "Kate", "data": {"age": 30, "number": 12345}},
    {"name": "Petr", "data": {"age": 2, "status": "self-employed"}},
    {"name": "A", "data": {"age": 101, "job": "doctor"}}
])
def test_create_object_with_different_testdata(body, start_end_testing_print):
    headers = {"Content-Type": "application/json"}
    response = requests.post(base_url, json=body, headers=headers)
    assert response.status_code == 200, f'Expected status code is 200, the actual one is {response.status_code}'


def test_get_object_id(get_new_object_id):
    response = requests.get(f'{base_url}/{get_new_object_id}').json()
    assert get_new_object_id == response['id']


@pytest.mark.medium
def test_update_new_object_with_put_method(get_new_object_id):
    body = {
        "name": "Ivan",
        "data": {
            "age": 30,
            "job": "doctor",
            "location": "Minsk"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(f'{base_url}/{get_new_object_id}', json=body, headers=headers).json()
    assert response['data']['location'] == 'Minsk', "object location is incorrect"


def test_update_new_object_with_patch_method(get_new_object_id):
    body = {
        "data": {
            "age": 31
        }
    }
    headers = {"Content-Type": "application/json"}

    response = requests.patch(f'{base_url}/{get_new_object_id}', json=body, headers=headers).json()
    assert response['data']['age'] == 31, 'object age is incorrect'


def test_delete_object(get_new_object_id):
    requests.delete(f'{base_url}/{get_new_object_id}')
    response = requests.get(f'{base_url}/{get_new_object_id}')
    assert response.status_code == 404
