import time
import pytest
from ..PageObject.URLs import Urls
from ..PageObject.base_page import BasePage
from ..PageObject.login_page import LoginPage, user_registration_creds
from ..PageObject.react_admin_page import ReactAdminPage


class TestSalesUser:
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
        logout_page.user_login(user_registration_creds()[0], user_registration_creds()[1])
        sales_user_page = ReactAdminPage(browser)
        sales_user_page.go_to_sales_user()
        time.sleep(2)
