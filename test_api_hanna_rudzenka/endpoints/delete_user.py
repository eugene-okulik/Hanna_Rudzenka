import requests
import allure

from endpoints.base_endpoint import Endpoint


class DeleteUser(Endpoint):
    @allure.step('Delete a user by id')
    def delete_user_by_id(self, user_id):
        self.response = requests.delete(f'{self.base_url}/{user_id}')
        print(self.response)
