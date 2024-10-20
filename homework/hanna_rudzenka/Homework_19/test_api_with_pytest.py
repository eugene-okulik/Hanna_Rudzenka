import pytest
import requests
import allure

base_url = 'http://167.172.172.115:52353/object'


@allure.feature('Users')
@allure.story('Create users with diff test data')
@allure.title('Добавление новых пользователей с разными тестовыми данными')
@pytest.mark.critical
@pytest.mark.parametrize('body', [
    {"name": "Kate", "data": {"age": 30, "number": 12345}},
    {"name": "Petr", "data": {"age": 2, "status": "self-employed"}},
    {"name": "A", "data": {"age": 101, "job": "doctor"}}
])
def test_create_user_with_different_testdata(body, start_end_testing_print):
    headers = {"Content-Type": "application/json"}
    with allure.step('Add a new user'):
        response = requests.post(base_url, json=body, headers=headers)
    with allure.step('Check that after adding a new user status code 200 is returned'):
        assert response.status_code == 200, f'Expected status code is 200, the actual one is {response.status_code}'


@allure.feature('Users')
@allure.title('Проверка правильный ли id возвращается для существующего юзера')
def test_get_user_id(get_new_object_id):
    with allure.step('Get json response data for user'):
        response = requests.get(f'{base_url}/{get_new_object_id}').json()
    with allure.step(f'Check that {get_new_object_id} is returned in response data '):
        assert get_new_object_id == response['id']


@allure.feature('Users')
@allure.story('Update a new user data with "put" method')
@allure.title('Обноваление данных пользователя при помощи метода put')
@pytest.mark.medium
def test_update_new_user_with_put_method(get_new_object_id):
    body = {
        "name": "Ivan",
        "data": {
            "age": 30,
            "job": "doctor",
            "location": "Minsk"
        }
    }
    headers = {"Content-Type": "application/json"}
    with allure.step('Updating user data by adding "location" field '):
        response = requests.put(f'{base_url}/{get_new_object_id}', json=body, headers=headers).json()
    with allure.step('Verify that "location" field has value "Minsk" '):
        assert response['data']['location'] == 'Minsk', "user location is incorrect"


@allure.feature('Users')
@allure.story('Update a new user data with "patch" method')
@allure.title('Обновление данных пользователя при помощи метода patch')
def test_update_new_user_with_patch_method(get_new_object_id):
    body = {
        "data": {
            "age": 31
        }
    }
    headers = {"Content-Type": "application/json"}
    with allure.step('Update a new user data by changing the value of "age" field'):
        response = requests.patch(f'{base_url}/{get_new_object_id}', json=body, headers=headers).json()
    with allure.step('Verify that "age" field has value 31'):
        assert response['data']['age'] == 31, 'user age is incorrect'


@allure.feature('Users')
@allure.story('Delete a new user')
@allure.title('Удаление пользователя по id')
def test_delete_user(get_new_object_id):
    with allure.step('Delete a new user by id'):
        requests.delete(f'{base_url}/{get_new_object_id}')
    with allure.step('Get data of a deleted user'):
        response = requests.get(f'{base_url}/{get_new_object_id}')
    with allure.step('Check that the status code is 404'):
        assert response.status_code == 404
