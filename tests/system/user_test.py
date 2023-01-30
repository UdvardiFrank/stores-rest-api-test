from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/register', data={'username': 'test', 'password': '1234'})


    def test_register_and_login(self):
        pass

    def test_register_duplicate_user(self):
        pass