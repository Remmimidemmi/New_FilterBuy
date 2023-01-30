from .locators import LoginPageLocators, MainPageLocators
from .URLs import RegistrationCreds
import random
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.browser.current_url)

    def account_page(self):
        self.browser.find_element(*MainPageLocators.MY_ACCOUNT_BUTTON).click()

    def hello_message(self):
        hello_user = self.browser.find_element(*MainPageLocators.HELLO_USERNAME)
        text_hello_user = hello_user.text
        user_name = text_hello_user[7:]
        return user_name

    def reg_hello_message_check(self):
        assert self.hello_message() == RegistrationCreds.FIRST_NAME, "Registration failed!"
        print(f'Success! {self.hello_message()} is register!')

    def reg_sales_user(self):
        self.browser.find_element(*MainPageLocators.REQUEST_SALES_USER_FIELD).send_keys("Test" + str(
            random.randint(1, 99999)))
        self.browser.find_element(*MainPageLocators.BECOME_SALES_USER_BUTTON).click()