import time

from .base_page import BasePage
from .data import NewCustomerData
from .locators import NewCustomersLocators

class SalesUserPage(BasePage):
    def new_customer_information(self):
        self.browser.find_element(*NewCustomersLocators.BUSINESS_NAME).send_keys(NewCustomerData.BUSINESS_NAME)
        self.browser.find_element(*NewCustomersLocators.TAX_EXEMPT_CHECKBOX).click()
        self.browser.find_element(*NewCustomersLocators.CREDIT_TERMS_CHECKBOX).click()
        time.sleep(5)