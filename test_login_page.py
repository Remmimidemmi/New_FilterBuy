import time
from .PageObject.login_page import LoginPage
from .PageObject.URLs import Urls
import pytest


@pytest.mark.test_1
def test_reg_new_common_user(browser):
    browser.get(Urls.REACT_MAIN_PAGE)
    page = LoginPage(browser)
    # page.open()
    page.account_page()
    page.common_user_registration()


@pytest.mark.test_2
def test_log_common_user(browser):
    browser.get(Urls.REACT_MAIN_PAGE)
    page = LoginPage(browser)
    page.account_page()
    page.common_user_login()

