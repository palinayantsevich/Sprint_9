from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    CREATE_RECIPE_FORM = (By.XPATH, '//form[@class="styles_form__2nwxz styles_form__3XFkE"]')
    RECIPE_NAME_INPUT_FIELD = (
    By.XPATH, '//div[text()="Название рецепта"]/following-sibling::input[@class="styles_inputField__3eqTj"]')
    BREAKFAST_CHECKBOX = (By.XPATH,
                          '//span[text()="Завтрак"]/preceding-sibling::button[@class="styles_checkbox__1WBUC styles_checkboxGroupItem__1aTHO styles_checkbox_active__22dG2"]')
    INGREDIENTS_INPUT_FIELD = (By.XPATH, '//input[@class="styles_inputField__3eqTj styles_ingredientsInput__1zzql"]')
    AMOUNT_INPUT_FIELD = (By.XPATH, '//input[@class="styles_inputField__3eqTj styles_ingredientsAmountValue__2matT"]')
    ADD_INGREDIENT_BUTTON = (By.XPATH, '//div[text()="Добавить ингредиент"]')
    TIME_COOKING_INPUT_FIELD = (
    By.XPATH, '//div[text()="Время приготовления"]/following-sibling::input[@class="styles_inputField__3eqTj"]')
    RECIPE_DESCRIPTION_TEXTAREA = (By.XPATH, '//textarea[@class="styles_textareaField__1wfhC"]')
    UPLOAD_FILE_BUTTON = (By.XPATH, '//input[@class="styles_fileInput__3HjP3"]')
    CREATE_RECIPE_BUTTON = (By.XPATH, '//button[text()="Создать рецепт"]')
    RECIPE_CARD_CREATED = (By.XPATH, '//div[@class="styles_single-card__1yTTj"]')
    RECIPE_NAME_CREATED = (By.XPATH, '//h1[@class="styles_single-card__title__2QMPq"]')

    def build_add_ingredient_locator(self, ingredient):
        return (By.XPATH, f'//div[text()="{ingredient}"]')
