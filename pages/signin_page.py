import allure

from pages.base_page import BasePage
from locators.signin_page_locators import SignInPageLocators


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignInPageLocators()

    @allure.step('Check that the signin form is displayed.')
    def check_signin_form_displayed(self):
        return self.wait_element_is_visible(self.locators.SIGNIN_FORM)

    @allure.step('Fill the sign-in form.')
    def wait_fill_signin_form(self, email, password):
        self.check_signin_form_displayed()
        self.wait_element_is_visible(self.locators.EMAIL_INPUT_FIELD)
        self.fill_input(self.locators.EMAIL_INPUT_FIELD, email)
        self.fill_input(self.locators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Click on the "Войти" button.')
    def wait_click_on_signin_button(self):
        self.wait_element_is_clickable(self.locators.SIGNIN_BUTTON)
        self.click_on_element(self.locators.SIGNIN_BUTTON)

    @allure.step('Log in user.')
    def login_user(self, email, password):
        self.wait_fill_signin_form(email, password)
        self.wait_click_on_signin_button()
