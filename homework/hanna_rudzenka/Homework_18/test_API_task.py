import requests
import allure

base_url = 'http://167.172.172.115:52353/object'


def get_user_id():
    body = {
        "name": "Ivan",
        "data": {
            "age": 30,
            "job": "doctor"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(base_url, json=body, headers=headers).json()
    return response['id']


def clear_user(user_id):
    requests.delete(f'{base_url}/{user_id}')


@allure.feature('Users')
@allure.story('Create a new user')
@allure.title('Создание нового пользователя')
def test_create_new_user():
    body = {
        "name": "Kate",
        "data": {
            "age": 30,
            "job": "doctor"
        }
    }
    headers = {"Content-Type": "application/json"}
    with allure.step('Add a new user'):
        response = requests.post(base_url, json=body, headers=headers)
    with allure.step('Check that after creating a new user status code 200 is returned'):
        assert response.status_code == 200, f'Expected status code is 200, the actual one is {response.status_code}'


@allure.feature('Users')
@allure.story('Update a new user data with "put" method')
@allure.title('Обноваление данных пользователя при помощи метода put')
def test_update_new_user_with_put_method():
    with allure.step('Get id of created user'):
        user_id = get_user_id()
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
        response = requests.put(f'{base_url}/{user_id}', json=body, headers=headers).json()
    with allure.step('Verify that "location" field has value "Minsk" '):
        assert response['data']['location'] == 'Minsk', "user location is incorrect"
    with allure.step('Delete a user'):
        clear_user(user_id)


@allure.feature('Users')
@allure.story('Update a new user data with "patch" method')
@allure.title('Обновление данных пользователя при помощи метода patch')
def test_update_new_user_with_patch_method():
    with allure.step('Create a new user'):
        user_id = get_user_id()
    body = {
        "data": {
            "age": 31
        }
    }
    headers = {"Content-Type": "application/json"}
    with allure.step('Update a new user data by changing the value of "age" field'):
        response = requests.patch(f'{base_url}/{user_id}', json=body, headers=headers).json()
    with allure.step('Verify that "age" field has value 31'):
        assert response['data']['age'] == 31, 'user age is incorrect'
    with allure.step('Delete user'):
        clear_user(user_id)


@allure.feature('Users')
@allure.story('Delete a user')
@allure.title('Удаление пользователя по id')
def test_delete_user():
    with allure.step('Add a new user'):
        user_id = get_user_id()
    with allure.step('Delete a new user by id'):
        requests.delete(f'{base_url}/{user_id}')
    with allure.step('Get data of a deleted user'):
        response = requests.get(f'{base_url}/{user_id}')
    with allure.step('Check that the status code is 404'):
        assert response.status_code == 404
