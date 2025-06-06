import allure

from pages.base_page import BasePage
from locators.signup_page_locators import SignUpPageLocators
from urls import Urls
from helper import Helper


class SignUpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignUpPageLocators()

    @allure.step('Wait until the "Signup Page" is loaded.')
    def wait_for_load_signup_page(self):
        return self.wait_load_page_by_checking_url(Urls.SIGNUP_PAGE)

    @allure.step('Fill the registration form.')
    def wait_fill_registration_form(self):
        self.wait_element_is_visible(self.locators.REGISTRATION_FORM)
        self.wait_element_is_visible(self.locators.NAME_INPUT_FIELD)
        self.fill_input(self.locators.NAME_INPUT_FIELD, Helper.generate_first_name())
        self.fill_input(self.locators.SURNAME_INPUT_FIELD, Helper.generate_last_name())
        self.fill_input(self.locators.USER_NAME_INPUT_FIELD, Helper.generate_username())
        self.fill_input(self.locators.EMAIL_INPUT_FIELD, Helper.generate_user_email())
        self.fill_input(self.locators.PASSWORD_INPUT_FIRLD, Helper.generate_user_password())

    @allure.step('Click on the "Создать аккаунт" button.')
    def wait_click_on_create_account_button(self):
        self.wait_element_is_clickable(self.locators.CREATE_ACCOUNT_BUTTON)
        self.click_on_element(self.locators.CREATE_ACCOUNT_BUTTON)
