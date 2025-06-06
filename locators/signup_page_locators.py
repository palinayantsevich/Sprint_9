from selenium.webdriver.common.by import By


class SignUpPageLocators:
    REGISTRATION_FORM = (By.XPATH, '//form[@class="styles_form__2nwxz styles_form__24nV3"]')
    NAME_INPUT_FIELD = (By.XPATH, '//input[@name="first_name"]')
    SURNAME_INPUT_FIELD = (By.XPATH, '//input[@name="last_name"]')
    USER_NAME_INPUT_FIELD = (By.XPATH, '//input[@name="username"]')
    EMAIL_INPUT_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT_FIRLD = (By.XPATH, '//input[@name="password"]')
    CREATE_ACCOUNT_BUTTON = (
    By.XPATH, '//button[@class="style_button__1FFWl styles_button__146Sy style_button_style_dark-blue__1cpq7"]')
