import pytest

from endpoints.create_user import CreateUser
from endpoints.delete_user import DeleteUser
from endpoints.get_user import GetUser
from endpoints.update_user import UpdateUser


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
