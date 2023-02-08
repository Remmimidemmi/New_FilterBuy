import time
import pytest

from ..PageObject.sales_user_page import SalesUserPage
from ..PageObject.data import LogInCreds, NewCustomerData, RegistrationCreds
from ..PageObject.URLs import Urls
from ..PageObject.base_page import BasePage
from ..PageObject.login_page import LoginPage
from ..PageObject.react_admin_page import ReactAdminPage
from ..PageObject.inscriptions import ErrorMessages
from ..PageObject.locators import NewCustomersLocators


class TestSalesUserReg:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.common_user_registration()

    @pytest.mark.test_1
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
        sales_user_page = SalesUserPage(browser)
        sales_user_page.go_to_sales_user()
        time.sleep(2)


class TestNewCustomer():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.get(Urls.REACT_MAIN_PAGE)
        page = LoginPage(browser)
        page.account_page()
        page.user_login(LogInCreds.SIGN_IN_EMAIL_SALES, LogInCreds.SIGN_IN_PASSWORD)

    @pytest.mark.test_2
    def test_new_customer_without_shipping_address(self, browser):
        page = SalesUserPage(browser)
        page.go_to_sales_user()
        page.new_customer_correct_email()
        page.new_customer_information(NewCustomerData.BUSINESS_NAME)
        page.new_main_contact()
        page.submit_button()
        page.new_customer_check()

    @pytest.mark.test_3
    def test_new_customer_with_shipping_address(self, browser):
        page = SalesUserPage(browser)
        page.go_to_sales_user()
        page.new_customer_correct_email()
        page.new_customer_information(NewCustomerData.BUSINESS_NAME)
        page.new_main_contact()
        page.new_shipping_address()
        page.submit_button()
        page.new_customer_check()

    @pytest.mark.test_4
    def test_new_customer_with_filling_spaces(self, browser):
        page = SalesUserPage(browser)
        page.go_to_sales_user()
        page.new_customer_correct_email()
        page.new_customer_information("           ")
        page.new_main_contact()
        page.error_message(NewCustomersLocators.EMPTY_FIELD_NEW_CUSTOMER_MESSAGE,
                           ErrorMessages.EMPTY_FIELD_ERROR_MESSAGE)

    @pytest.mark.test_5
    def test_new_customer_incorrect_email(self, browser):
        page = SalesUserPage(browser)
        page.go_to_sales_user()
        page.new_customer_incorrect_email()
        page.new_customer_information(NewCustomerData.BUSINESS_NAME)
        page.new_main_contact()
        page.new_shipping_address()
        page.submit_button()

    @pytest.mark.test_6
    def test_mask_button_from_customers(self, browser):
        page = SalesUserPage(browser)
        page.go_to_sales_user()
        page.go_to_mask_user()

    @pytest.mark.test_7
    def test_customers_details(self, browser):
        page = SalesUserPage(browser)
        page.go_to_sales_user()
        page.go_to_customer_details()

    # @pytest.mark.test_test
    # def test_test(self, browser):
    #     page = SalesUserPage(browser)
    #     page.go_to_sales_user()
    #     page.go_to_customers_tab()
    #     time.sleep(15)
