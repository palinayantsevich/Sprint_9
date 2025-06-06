from selenium.webdriver.common.by import By


class SignInPageLocators:
    SIGNIN_FORM = (By.XPATH, '//form[@class="styles_form__2nwxz styles_form__2_42b"]')
    EMAIL_INPUT_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="password"]')
    SIGNIN_BUTTON = (
    By.XPATH, '//button[@class="style_button__1FFWl styles_button__1jD3X style_button_style_dark-blue__1cpq7"]')
