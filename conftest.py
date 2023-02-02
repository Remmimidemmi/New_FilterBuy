import pytest
from selenium import webdriver
session = None


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome("/home/user/New_FilterBuy/chromedriver")
    browser.set_window_size(1440, 1080)
    yield browser
    browser.quit()


