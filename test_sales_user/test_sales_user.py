import time
import pytest

from ..PageObject.data import LogInCreds
from ..PageObject.URLs import Urls
from ..PageObject.base_page import BasePage
from ..PageObject.login_page import LoginPage
from ..PageObject.react_admin_page import ReactAdminPage



class TestSalesUserReg:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.common_user_registration()

    def test_register_sales_user(self, browser):
        browser.get(Urls.REACT_REQUEST_NEW_SALES_USER)
        page = BasePage(browser)
        page.reg_sales_user()
        browser.get(Urls.ADMIN_OUTSIDE_USERS)
        admin_page = ReactAdminPage(browser)
        admin_page.login_admin()
        admin_page.activate_checkbox_from_outside_salers()
        browser.get(Urls.REACT_MAIN_PAGE)
        logout_page = LoginPage(browser)
        logout_page.common_user_logout()
        logout_page.account_page()
        logout_page.login_after_registration()
        sales_user_page = ReactAdminPage(browser)
        sales_user_page.go_to_sales_user()
        time.sleep(2)


class TestNewCustomer():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.user_login(LogInCreds.SIGN_IN_EMAIL_SALES, LogInCreds.SIGN_IN_PASSWORD)

    @pytest.mark.test_1
    def test_new_customer_without_shipping_address(self, browser):
        page = ReactAdminPage(browser)
        page.go_to_sales_user()


