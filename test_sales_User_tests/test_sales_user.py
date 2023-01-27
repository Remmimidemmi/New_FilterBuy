import time
import pytest
from ..PageObject.URLs import Urls
from ..test_login_page import test_log_common_user
from ..PageObject.base_page import BasePage


class TestSalesUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        test_log_common_user(browser)

    def test_register_sales_user(self, browser):
        browser.get(Urls.REACT_REQUEST_NEW_SALES_USER)
        page = BasePage(browser)
        page.reg_sales_user()
