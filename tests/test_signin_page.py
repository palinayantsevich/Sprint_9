import pytest
import allure

from urls import Urls


class TestSignInPage:

    @allure.title(
        'Verify that after successful registration - user is navigated to the Main page and the "Выход" button is displayed.')
    def test_login_user_logged_in_successfully(self, driver, main_page, generate_user_data, register_user, signin_page):
        signin_page.open_page(Urls.SIGNIN_PAGE)
        signin_page.check_signin_form_displayed()
        signin_page.wait_fill_signin_form(generate_user_data['email'], generate_user_data['password'])
        signin_page.wait_click_on_signin_button()
        assert main_page.wait_load_page_by_checking_url(Urls.MAIN_PAGE)
        assert main_page.check_logout_button_is_displayed()
