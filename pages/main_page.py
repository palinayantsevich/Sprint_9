import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step('Click on "Создать аккаунт" button.')
    def wait_click_create_account_button(self):
        self.wait_element_is_visible(self.locators.CREATE_ACCOUNT_BUTTON)
        self.click_on_element(self.locators.CREATE_ACCOUNT_BUTTON)

    @allure.step('Check that the "Выход" button is displayed.')
    def check_logout_button_is_displayed(self):
        return self.wait_element_is_visible(self.locators.LOGOUT_BUTTON)

    @allure.step('Click on "Создать рецепт" button.')
    def wait_click_create_recipe_button(self):
        self.wait_element_is_visible(self.locators.CREATE_RECIPE_BUTTON)
        self.click_on_element(self.locators.CREATE_RECIPE_BUTTON)
