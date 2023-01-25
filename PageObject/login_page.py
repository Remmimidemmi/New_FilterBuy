from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def common_user_registration(self):
        email = "user_" + str(time.time()) + "@test.test"
        password = "123"
        f_name = "F_name"
        l_name = str(time.time())
        self.browser.find_element(*LoginPageLocators.SIGN_UP_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIRST_NAME).send_keys(f_name)
        self.browser.find_element(*LoginPageLocators.LAST_NAME).send_keys(l_name)
