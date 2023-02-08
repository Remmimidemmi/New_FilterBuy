import pytest

from selenium import webdriver
session = None


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome("/home/user/New_FilterBuy/chromedriver")
    browser.maximize_window()
    yield browser
    browser.quit()


