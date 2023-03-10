import time
import pytest
from selenium.common import NoSuchElementException

from ..PageObject.data import LogInCreds, RegistrationCreds
from ..PageObject.locators import LoginPageLocators
from ..PageObject.URLs import Urls
from ..PageObject.login_page import LoginPage
from ..PageObject.inscriptions import ErrorMessages
from ..mail import ReadLettersFromGmail


class TestPositive():
    @pytest.mark.test_1
    def test_reg_new_common_user(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.common_user_registration(email=RegistrationCreds.REGISTRATION_EMAIL_ONE)

    @pytest.mark.test_2
    def test_log_common_user(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.user_login(LogInCreds.SIGN_IN_EMAIL, LogInCreds.SIGN_IN_PASSWORD)
        page.hello_message()

    @pytest.mark.test_3
    def test_forgot_password_correct_email(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.forgot_password_login_page(email=LogInCreds.SIGN_IN_REAL_EMAIL)
        time.sleep(5)
        page.change_password_from_login_page(RegistrationCreds.PASSWORD)
        page.hello_message()


@pytest.mark.negative
class TestNegative():
    @pytest.mark.test_4
    def test_incorrect_pass_login(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.user_login(LogInCreds.SIGN_IN_EMAIL, LogInCreds.SIGN_IN_PASSWORD_INCORRECT)
        page.error_message(LoginPageLocators.ERROR_LOGIN_MESSAGE, ErrorMessages.LOGIN_ERROR_MESSAGE)
        page.error_link(LoginPageLocators.RESET_PASSWORD_LINK)

    @pytest.mark.test_5
    def test_incorrect_email_login(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.user_login(LogInCreds.SIGN_IN_EMAIL_INCORRECT, LogInCreds.SIGN_IN_PASSWORD)
        page.error_message(LoginPageLocators.ERROR_LOGIN_MESSAGE, ErrorMessages.LOGIN_ERROR_MESSAGE)
        page.error_link(LoginPageLocators.RESET_PASSWORD_LINK)

    @pytest.mark.test_6
    @pytest.mark.xfail
    def test_without_creds_login(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.signin_button()
        page.hello_message()

    @pytest.mark.test_7
    def test_forgot_password_incorrect_email(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.forgot_password_login_page(LogInCreds.SIGN_IN_EMAIL_INCORRECT)
        page.error_message(LoginPageLocators.ERROR_RESET_PASSWORD_MESSAGE,
                           ErrorMessages.ERROR_RESET_PASSWORD_MESSAGE)
        page.error_link(LoginPageLocators.SIGN_UP_LINK_AFTER_FORGOT)
# @pytest.mark.test_test
# def test_mail(browser):
#     page = ReadLettersFromGmail().return_link_for_reset_password()
#     #page.read_mess_from_email()
#     #return_link_for_reset_password()
