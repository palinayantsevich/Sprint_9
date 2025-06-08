import requests
import allure
from urls import Urls


class RegisterUserAPI:
    @staticmethod
    @allure.step('Register new user.')
    def register_user(user_data):
        headers = {"Content-Type": "application/json"}
        response = requests.post(Urls.REGISTER_USER_API, json=user_data, headers=headers)
        return response
