import pytest
import allure

from urls import Urls


class TestSignUpPage:

    @allure.title(
        'Verify that after successful registration - user is navigated to the Signin page.')
    def test_create_account_created_successfully(self, driver, main_page, signin_page, signup_page):
        main_page.wait_click_create_account_button()
        signup_page.wait_for_load_signup_page()
        signup_page.wait_fill_registration_form()
        signup_page.wait_click_on_create_account_button()
        assert signin_page.wait_load_page_by_checking_url(Urls.SIGNIN_PAGE)
        assert signin_page.check_signin_form_displayed()
