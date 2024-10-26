from locust import task, HttpUser


class User(HttpUser):
    headers = {"Content-Type": "application/json"}

    @task(weight=1)
    def create_user(self):
        response = self.client.post(
            'object',
            json={"name": "Kate", "data": {"age": 30, "number": 12345}},
            headers=self.headers
        ).json()
        return response['id']

    @task(weight=1)
    def check_user_id(self):
        user_id = self.create_user()
        self.client.get(
            f'object/{user_id}',
            headers=self.headers
        )
        self.delete_user_by_id(user_id)

    @task(weight=1)
    def update_user_with_put_method(self):
        user_id = self.create_user()
        self.client.put(
            f'object/{user_id}',
            json={"name": "Kate", "data": {"age": 15, "job": "doctor"}},
            headers=self.headers
        )
        self.delete_user_by_id(user_id)

    @task(weight=1)
    def update_user_with_patch_method(self):
        user_id = self.create_user()
        self.client.patch(
            f'object/{user_id}',
            json={"name": "Anton"},
            headers=self.headers
        )
        self.delete_user_by_id(user_id)

    def delete_user_by_id(self, user_id):
        self.client.delete(f'object/{user_id}',
                           headers=self.headers)

    @task(weight=1)
    def delete_user(self):
        user_id = self.create_user()
        self.client.delete(
            f'object/{user_id}',
            headers=self.headers
        )
