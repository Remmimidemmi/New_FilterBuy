import time
import pytest

from ..PageObject.URLs import Urls
from ..PageObject.login_page import LoginPage


class TestPositive():
    @pytest.mark.test_1
    def test_reg_new_common_user(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        # page.open()
        page.account_page()
        page.common_user_registration()

    @pytest.mark.test_2
    def test_log_common_user(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.common_user_login()


class TestNegative():
    @pytest.mark.test_3
    def test_incorrect_pass_login(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.incorrect_password_login()
        page.error_login_message()

    @pytest.mark.test_4
    def test_incorrect_email_login(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.incorrect_email_login()
        page.error_login_message()
