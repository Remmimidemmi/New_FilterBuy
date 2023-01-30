from selenium.common import NoSuchElementException, TimeoutException

from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators
from .URLs import RegistrationCreds, LogInCreds
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def user_registration_creds():
    registration_email = RegistrationCreds.REGISTRATION_EMAIL
    registration_password = RegistrationCreds.PASSWORD
    return [registration_email, registration_password]


class LoginPage(BasePage):

    def common_user_registration(self):
        self.browser.find_element(*LoginPageLocators.SIGN_UP_EMAIL).send_keys(
            user_registration_creds()[0]
        )
        self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWORD).send_keys(
            user_registration_creds()[1]
        )
        self.browser.find_element(*LoginPageLocators.SIGN_UP_CONFIRM_PASSWORD).send_keys(
            user_registration_creds()[1]
        )
        self.browser.find_element(*LoginPageLocators.FIRST_NAME).send_keys(
            RegistrationCreds.FIRST_NAME
        )
        self.browser.find_element(*LoginPageLocators.LAST_NAME).send_keys(
            RegistrationCreds.LAST_NAME
        )
        self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON).click()
        self.reg_hello_message_check()

    def user_login(self, email, password):
        self.browser.find_element(*LoginPageLocators.SiGN_IN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def common_user_logout(self):
        self.browser.find_element(*MainPageLocators.USER_MY_ACCOUNT_BUTTON).click()
        self.browser.find_element(*MainPageLocators.LOGOUT_BUTTON).click()

    # def repeat_login_after_registration(self):
    #     self.browser.find_element(*LoginPageLocators.SiGN_IN_EMAIL).send_keys(
    #         user_registration_creds()[0]
    #     )
    #     self.browser.find_element(*LoginPageLocators.SIGN_IN_PASSWORD).send_keys(
    #         user_registration_creds()[1]
    #     )
    #     self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON).click()

    def error_login_message(self):
        try:
            error_message = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
                LoginPageLocators.ERROR_LOGIN_MESSAGE
            ))
            text_error_message = error_message.text
            exp_message = "Invalid username/password. Please try again."
            assert text_error_message == exp_message, f"EXPECTED:\n{exp_message}\nACTUAL:\n{text_error_message}"
            print("Message correct!")
        finally:
            reset_link = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(
                LoginPageLocators.RESET_PASSWORD_LINK
            ))
            assert reset_link, "Link is not clickable!"
            print("Link is clickable!")

