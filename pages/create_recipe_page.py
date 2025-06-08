import allure

from pages.base_page import BasePage
from locators.create_recipe_page_locators import CreateRecipePageLocators
from urls import Urls


class CreateRecipePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CreateRecipePageLocators()

    @allure.step('Wait until the "Create Recipe Page" is loaded.')
    def wait_for_load_create_recipe_page(self):
        return self.wait_load_page_by_checking_url(Urls.CREATE_RECIPE_PAGE)

    @allure.step('Add the ingredients in the recipe creation form.')
    def add_ingredient_and_amount(self, ingredient, amount):
        self.fill_input(self.locators.INGREDIENTS_INPUT_FIELD, ingredient)
        self.wait_element_is_visible(self.locators.build_add_ingredient_locator(ingredient))
        self.click_on_element(self.locators.build_add_ingredient_locator(ingredient))
        self.fill_input(self.locators.AMOUNT_INPUT_FIELD, amount)
        self.click_on_element(self.locators.ADD_INGREDIENT_BUTTON)

    @allure.step('Fill text fields in the recipe creation form.')
    def wait_fill_text_fields_in_recipe_creation_form(self, recipe_name, time_value, description):
        self.wait_element_is_visible(self.locators.CREATE_RECIPE_FORM)
        self.wait_element_is_visible(self.locators.RECIPE_NAME_INPUT_FIELD)
        self.fill_input(self.locators.RECIPE_NAME_INPUT_FIELD, recipe_name)
        self.wait_element_is_clickable(self.locators.BREAKFAST_CHECKBOX)
        self.click_on_element(self.locators.BREAKFAST_CHECKBOX)
        self.fill_input(self.locators.TIME_COOKING_INPUT_FIELD, time_value)
        self.fill_input(self.locators.RECIPE_DESCRIPTION_TEXTAREA, description)

    @allure.step('Click on the "Создать рецепт" button.')
    def wait_click_on_create_recipe_button(self):
        self.wait_element_is_clickable(self.locators.CREATE_RECIPE_BUTTON)
        self.click_on_element(self.locators.CREATE_RECIPE_BUTTON)

    @allure.step('Check that the recipe card is displayed.')
    def check_recipe_card_displayed(self):
        return self.wait_element_is_visible(self.locators.RECIPE_CARD_CREATED)

    @allure.step('Check the name of the created recipe.')
    def check_created_recipe_name(self):
        self.wait_element_is_visible(self.locators.RECIPE_NAME_CREATED)
        return self.get_element_text(self.locators.RECIPE_NAME_CREATED)

    @allure.step('Upload recipe image.')
    def upload_recipe_image(self, image_path):
        self.upload_file(self.locators.UPLOAD_FILE_BUTTON, image_path)
