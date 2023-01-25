import time

from .PageObject.login_page import LoginPage


def test_new_try(browser):
    browser.get("https://react.test.filterbuytest.com/my-account/login/?next=/my-account/")
    page = LoginPage(browser)
    page.open()
    time.sleep(2)
    page.common_user_registration()