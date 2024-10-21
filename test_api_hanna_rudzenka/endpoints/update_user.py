import requests
import allure

from endpoints.base_endpoint import Endpoint


class UpdateUser(Endpoint):
    @allure.step('Update user data with put method')
    def update_user_with_put_method(self, body, user_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.base_url}/{user_id}', json=body, headers=headers)
        self.json = self.response.json()

    @allure.step('Update user data with patch method')
    def update_user_with_patch_method(self, body, user_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.base_url}/{user_id}', json=body, headers=headers)
        self.json = self.response.json()
