import pytest
import allure
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import os

from pages.signup_page import SignUpPage
from urls import Urls
from helper import Helper
from pages.main_page import MainPage
from pages.signin_page import SignInPage
from pages.create_recipe_page import CreateRecipePage
from api.user_api import RegisterUserAPI


@pytest.fixture(scope='function')
def driver():
    with allure.step('Open browser.'):
        selenoid_url = os.getenv('SELENOID_URL', 'http://selenoid:4444/wd/hub')

        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--headless=new')

        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
        driver.get(Urls.MAIN_PAGE)

    yield driver

    with allure.step('Close browser.'):
        driver.quit()


@pytest.fixture(scope='function')
def generate_user_data():
    name = Helper.generate_first_name()
    surname = Helper.generate_last_name()
    nickname = Helper.generate_username()
    email = Helper.generate_user_email()
    password = Helper.generate_user_password()
    payload = {
        'first_name': name,
        'last_name': surname,
        'username': nickname,
        'email': email,
        'password': password
    }

    return payload


@pytest.fixture(scope='function')
def main_page(driver):
    main_page = MainPage(driver)
    return main_page


@pytest.fixture(scope='function')
def signin_page(driver):
    signin_page = SignInPage(driver)
    return signin_page


@pytest.fixture(scope='function')
def signup_page(driver):
    signup_page = SignUpPage(driver)
    return signup_page


@pytest.fixture(scope='function')
def create_recipe_page(driver):
    create_recipe_page = CreateRecipePage(driver)
    return create_recipe_page


@pytest.fixture(scope='function')
@allure.step('Register new user.')
def register_user(generate_user_data):
    RegisterUserAPI.register_user(generate_user_data)


@pytest.fixture(scope='function')
def recipe_name():
    recipe_name = Helper.generate_recipe_name()
    return recipe_name
