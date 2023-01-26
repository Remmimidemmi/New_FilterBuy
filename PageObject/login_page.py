from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators
from .URLs import RegistrationCreds, LogInCreds
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage(BasePage):

    def common_user_registration(self):
        self.browser.find_element(*LoginPageLocators.SIGN_UP_EMAIL).send_keys(RegistrationCreds.REGISTRATION_EMAIL)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWORD).send_keys(RegistrationCreds.PASSWORD)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_CONFIRM_PASSWORD).send_keys(RegistrationCreds.PASSWORD)
        self.browser.find_element(*LoginPageLocators.FIRST_NAME).send_keys(RegistrationCreds.FIRST_NAME)
        self.browser.find_element(*LoginPageLocators.LAST_NAME).send_keys(RegistrationCreds.LAST_NAME)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON).click()
        self.reg_hello_message_check()

    def common_user_login(self):
        self.browser.find_element(*LoginPageLocators.SiGN_IN_EMAIL).send_keys(LogInCreds.SIGN_IN_EMAIL)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_PASSWORD).send_keys(LogInCreds.SIGN_IN_PASSWORD)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()
        self.hello_message()
