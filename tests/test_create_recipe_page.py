import pytest
import allure

from urls import Urls
from data.data import RecipeData


class TestCreateRecipePage:

    @allure.title(
        'Verify that user can successfully create a recipe.')
    def test_create_recipe_created_successfully(self, driver, main_page, signin_page, generate_user_data, register_user,
                                                create_recipe_page, recipe_name):
        signin_page.open_page(Urls.SIGNIN_PAGE)
        signin_page.login_user(generate_user_data['email'], generate_user_data['password'])
        main_page.wait_click_create_recipe_button()
        create_recipe_page.wait_for_load_create_recipe_page()
        create_recipe_page.wait_fill_text_fields_in_recipe_creation_form(recipe_name, RecipeData.TIME_VALUE,
                                                                         RecipeData.RECIPE_DESCRIPTION)
        for ingredient, amount in RecipeData.INGREDIENTS:
            create_recipe_page.add_ingredient_and_amount(ingredient, amount)
        create_recipe_page.upload_recipe_image(RecipeData.IMAGE_PATH)
        create_recipe_page.wait_click_on_create_recipe_button()
        assert create_recipe_page.check_recipe_card_displayed()
        assert create_recipe_page.check_created_recipe_name() == recipe_name
