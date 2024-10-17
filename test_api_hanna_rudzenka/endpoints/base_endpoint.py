import allure


class Endpoint:
    base_url = 'http://167.172.172.115:52353/object'
    response = None
    json = None
    headers = {"Content-Type": "application/json"}

    @allure.step('Check that response is 200')
    def check_that_status_200(self):
        assert self.response.status_code == 200, (f'Expected status code is 200, '
                                                  f'the actual is {self.response.status_code}')

    @allure.step('Check that response is 404')
    def check_that_status_404(self):
        assert self.response.status_code == 404, (f'Expected status code is 404, '
                                                  f'the actual is {self.response.status_code}')

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.json["name"] == name, (f'expected value for field "name" is {name} '
                                           f'the actual value is {self.json["name"]}')

    @allure.step('Check that id is correct in response data')
    def check_response_id_is_correct(self, user_id):
        assert self.json["id"] == user_id, (f'expected value for field "id" is {user_id} '
                                            f'the actual value is {self.json["id"]}')

    @allure.step('Check that age is the same as sent')
    def check_response_age_is_correct(self, age):
        assert self.json['data']['age'] == age, (f'expected value for field "age" is {age} '
                                                 f'the actual value is {self.json['data']['age']}')
