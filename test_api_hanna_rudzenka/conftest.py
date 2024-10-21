import pytest
import requests

from endpoints.create_user import CreateUser
from endpoints.delete_user import DeleteUser
from endpoints.get_user import GetUser
from endpoints.update_user import UpdateUser
from endpoints.base_endpoint import Endpoint


@pytest.fixture()
def create_user_object():
    return CreateUser()


@pytest.fixture()
def get_user_data_object():
    return GetUser()


@pytest.fixture()
def update_user_object():
    return UpdateUser()


@pytest.fixture()
def delete_user_object():
    return DeleteUser()


@pytest.fixture()
def create_user_and_get_id(create_user_object, delete_user_object):
    body = {"name": "Ivan", "data": {"age": 30, "job": "doctor"}}
    create_user_object.create_user(body)
    user_id = create_user_object.json['id']
    yield create_user_object.json['id']
    delete_user_object.delete_user_by_id(user_id)
