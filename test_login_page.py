import time
import pytest

from .PageObject.URLs import Urls
from .PageObject.login_page import LoginPage
from .PageObject.react_admin_page import ReactAdminPage


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


# @pytest.mark.test_3
# def test_try_to_outside(browser):
#     browser.get(Urls.ADMIN_REACT_PAGE)
#     page = ReactAdminPage(browser)
#     page.login_admin()
#     page.go_to_outside_salers()
