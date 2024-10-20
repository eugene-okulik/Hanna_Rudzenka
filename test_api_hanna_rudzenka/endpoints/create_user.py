import allure
import requests
from endpoints.base_endpoint import Endpoint


class CreateUser(Endpoint):
    @allure.step('Check that response is 200 when create a user')
    def create_user(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.base_url, json=body, headers=headers)
        self.json = self.response.json()
        return self.json
