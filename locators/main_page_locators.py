from selenium.webdriver.common.by import By


class MainPageLocators:
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//a[text()="Создать аккаунт"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[text()="Выход"]')
    CREATE_RECIPE_BUTTON = (By.XPATH, '//a[text()="Создать рецепт"]')
