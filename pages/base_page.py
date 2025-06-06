import allure
from pathlib import Path

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait_time=15):
        self.driver = driver
        self.wait_time = wait_time

    @allure.step('Open page: {url}.')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Wait until the element is displayed: {locator}.')
    def wait_element_is_visible(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located(locator))

    @allure.step('Wait until the element is clickable: {locator}.')
    def wait_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, self.wait_time).until(EC.element_to_be_clickable(locator))

    @allure.step('Click on element: {locator}.')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Fill the input field {locator} with value: {text}.')
    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Wait until the page is loaded and check page url: {url}.')
    def wait_load_page_by_checking_url(self, url):
        return WebDriverWait(self.driver, self.wait_time).until(EC.url_to_be(url))

    @allure.step('Wait until the page is loaded and check page url: {url}.')
    def wait_load_page_by_checking_url(self, url):
        return WebDriverWait(self.driver, self.wait_time).until(EC.url_to_be(url))

    @allure.step('Get text of the element: {locator}.')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Upload file.')
    def upload_file(self, locator, file_path):
        if isinstance(file_path, Path):
            file_path = str(file_path)

        self.driver.find_element(*locator).send_keys(file_path)
