import pytest

CREATE_USER_TEST_DATA = {"name": "Ivan", "data": {"age": 30, "job": "doctor"}}
CREATE_USERS_TEST_DATA = [
    {"name": "Kate", "data": {"age": 30, "number": 12345}},
    {"name": "Petr", "data": {"age": 2, "status": "self-employed"}},
    {"name": "A", "data": {"age": 101, "job": "doctor"}}
]


def test_create_user(create_user_object):
    create_user_object.create_user_and_get_id(CREATE_USER_TEST_DATA)
    create_user_object.check_that_status_200()
    create_user_object.check_response_name_is_correct('Ivan')


@pytest.mark.parametrize('body', CREATE_USERS_TEST_DATA)
def test_create_users(create_user_object, body):
    create_user_object.create_user_and_get_id(body)
    create_user_object.check_that_status_200()


def test_check_user_id(create_user_object, get_user_data_object):
    user_id = create_user_object.create_user_and_get_id(CREATE_USER_TEST_DATA)
    get_user_data_object.get_userdata_by_id(user_id)
    get_user_data_object.check_response_id_is_correct(user_id)


def test_update_user_with_put_method(create_user_object, update_user_object):
    user_id = create_user_object.create_user_and_get_id(CREATE_USER_TEST_DATA)
    update_user_object.update_user_with_put_method(body={"name": "Kate", "data": {"age": 15, "job": "doctor"}},
                                                   user_id=user_id)
    update_user_object.check_that_status_200()
    update_user_object.check_response_name_is_correct('Kate')
    update_user_object.check_response_age_is_correct(15)


def test_update_user_with_patch_method(create_user_object, update_user_object):
    user_id = create_user_object.create_user_and_get_id(CREATE_USER_TEST_DATA)
    update_user_object.update_user_with_patch_method(body={"name": "Anton"}, user_id=user_id)
    update_user_object.check_that_status_200()
    update_user_object.check_response_name_is_correct('Anton')
    update_user_object.check_response_age_is_correct(30)


def test_delete_user(create_user_object, delete_user_object):
    user_id = create_user_object.create_user_and_get_id(CREATE_USER_TEST_DATA)
    delete_user_object.delete_user_by_id(user_id)
