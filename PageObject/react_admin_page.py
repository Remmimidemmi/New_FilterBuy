import time
from ..PageObject.URLs import AdminCreds, LogInCreds
from ..PageObject.base_page import BasePage
from ..PageObject.locators import ReactAdminLocators, MainPageLocators


class ReactAdminPage(BasePage):
    def login_admin(self):
        self.browser.find_element(*ReactAdminLocators.SIGN_IN_EMAIL).send_keys(
            AdminCreds.REACT_ADMIN
        )
        self.browser.find_element(*ReactAdminLocators.SIGN_IN_PASSWORD).send_keys(
            LogInCreds.SIGN_IN_PASSWORD
        )
        self.browser.find_element(*ReactAdminLocators.LOGIN_BUTTON).click()

    def activate_checkbox_from_outside_salers(self):
        self.browser.find_element(*ReactAdminLocators.FIRST_CHECKBOX_ACTIVE).click()
        self.browser.find_element(*ReactAdminLocators.SAVE_BUTTON).click()

    def go_to_sales_user(self):
        self.browser.find_element(*MainPageLocators.USER_MY_ACCOUNT_BUTTON).click()
        self.browser.find_element(*MainPageLocators.SALES_LINK_TAB).click()

    # def repeat_login(self):

    # def go_to_outside_salers(self):
    #     self.browser.find_element(By.CSS_SELECTOR, "#adminmenu > li:nth-child(3) > a").click()
    #     self.browser.find_element(
    #         By.CSS_SELECTOR, "#adminmenu > li:nth-child(3) > div.wp-submenu > div > ul > li:nth-child(10) > a").click()
    #     self.browser.find_element(
    #         By.CSS_SELECTOR, "#content-main > div > table > tbody > tr.model-outsidesalesuser > th > a").click()
