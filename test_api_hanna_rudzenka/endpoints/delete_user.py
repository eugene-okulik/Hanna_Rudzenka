import requests
import allure

from endpoints.base_endpoint import Endpoint


class DeleteUser(Endpoint):
    @allure.step('Delete a new user by id')
    def delete_user_by_id(self, user_id):
        requests.delete(f'{self.base_url}/{user_id}')
        with allure.step('Get data of a deleted user'):
            response = requests.get(f'{self.base_url}/{user_id}')
        assert response.status_code == 404, (f'Expected status code is 404, '
                                             f'the actual is {self.response.status_code}')
