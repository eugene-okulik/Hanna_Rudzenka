import requests

base_url = 'http://167.172.172.115:52353/object'


def get_object_id():
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


def clear_object(object_id):
    requests.delete(f'{base_url}/{object_id}')


def create_new_object():
    body = {
        "name": "Kate",
        "data": {
            "age": 30,
            "job": "doctor"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(base_url, json=body, headers=headers)
    assert response.status_code == 200, f'Expected status code is 200, the actual one is {response.status_code}'


def update_new_object_with_put_method():
    object_id = get_object_id()
    body = {
        "name": "Ivan",
        "data": {
            "age": 30,
            "job": "doctor",
            "location": "Minsk"
        }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(f'{base_url}/{object_id}', json=body, headers=headers).json()
    assert response['data']['location'] == 'Minsk', "object location is incorrect"
    clear_object(object_id)


def update_new_object_with_patch_method():
    object_id = get_object_id()
    body = {
        "data": {
            "age": 31
        }
    }
    headers = {"Content-Type": "application/json"}

    response = requests.patch(f'{base_url}/{object_id}', json=body, headers=headers).json()
    assert response['data']['age'] == 31, 'object age is incorrect'
    clear_object(object_id)


def delete_object():
    object_id = get_object_id()
    requests.delete(f'{base_url}/{object_id}')
    response = requests.get(f'{base_url}/{object_id}')
    assert response.status_code == 404
