import allure
import requests
from endpoints.base_endpoint import Endpoint


class CreateUser(Endpoint):
    user_id = None

    @allure.step('Send post request to create a user')
    def create_user(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.base_url, json=body, headers=headers)
        self.json = self.response.json()
        self.user_id = self.json['id']
        return self.json
