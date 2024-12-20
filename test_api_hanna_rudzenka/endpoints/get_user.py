import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetUser(Endpoint):
    @allure.step('send get request to receive user data')
    def get_userdata_by_id(self, user_id):
        self.response = requests.get(f'{self.base_url}/{user_id}')
        self.json = self.response.json()
