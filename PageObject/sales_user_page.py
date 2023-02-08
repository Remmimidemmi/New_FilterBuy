from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .data import NewCustomerData, RegistrationCreds
from .locators import NewCustomersLocators, MainPageLocators


class SalesUserPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.email = RegistrationCreds.REGISTRATION_EMAIL

    def new_customer_correct_email(self):
        self.browser.find_element(*NewCustomersLocators.EMAIL).send_keys(self.email)

    def new_customer_incorrect_email(self):
        self.browser.find_element(*NewCustomersLocators.EMAIL).send_keys(RegistrationCreds.INCORRECT_REGISTRATION_EMAIL)

    def go_to_sales_user(self):
        self.browser.find_element(*MainPageLocators.USER_MY_ACCOUNT_BUTTON).click()
        self.browser.find_element(*MainPageLocators.SALES_LINK_TAB).click()

    def new_customer_information(self, business_name):
        self.browser.find_element(*NewCustomersLocators.BUSINESS_NAME).send_keys(business_name)
        self.browser.find_element(*NewCustomersLocators.TAX_EXEMPT_CHECKBOX).click()
        self.browser.find_element(*NewCustomersLocators.CREDIT_TERMS_CHECKBOX).click()

    def new_main_contact(self):
        self.browser.find_element(*NewCustomersLocators.FIRST_NAME).send_keys(RegistrationCreds.FIRST_NAME)
        self.browser.find_element(*NewCustomersLocators.LAST_NAME).send_keys(RegistrationCreds.LAST_NAME)
        self.browser.find_element(*NewCustomersLocators.PHONE_NUMBER).click()
        self.browser.find_element(*NewCustomersLocators.PHONE_NUMBER).send_keys(NewCustomerData.PHONE_NUMBER)
        # btn = self.browser.find_element(*NewCustomersLocators.SUBMIT_CUSTOMER_BTN)
        # self.browser.execute_script("arguments[0].scrollIntoView();", btn)
        # self.browser.execute_script("arguments[0].click();", btn)

    def new_shipping_address(self):
        self.browser.find_element(*NewCustomersLocators.COMPANY_NAME).send_keys(NewCustomerData.BUSINESS_NAME)
        self.browser.find_element(*NewCustomersLocators.ATTN).send_keys(NewCustomerData.ATTN)
        self.browser.find_element(*NewCustomersLocators.STREET_ADDRESS).send_keys(NewCustomerData.STREET_ADDRESS)
        self.browser.find_element(*NewCustomersLocators.TOWN_CITY).send_keys(NewCustomerData.TOWN_CITY)
        self.browser.find_element(*NewCustomersLocators.STATE).send_keys(NewCustomerData.STATE)
        self.browser.find_element(*NewCustomersLocators.STATE).send_keys(Keys.ENTER)
        self.browser.find_element(*NewCustomersLocators.POSTCODE_ZIP).send_keys(NewCustomerData.POSTCODE_ZIP)
        self.browser.find_element(*NewCustomersLocators.STATE).click()

    def submit_button(self):
        self.browser.find_element(*NewCustomersLocators.SUBMIT_CUSTOMER_BTN).click()

    def new_customer_check(self):
        new_customer_email = self.browser.find_element(*NewCustomersLocators.CUSTOMERS_LIST_NEW_CUSTOMER).text
        assert new_customer_email == self.email, "New customer is not found!"
        print(f"\nNew customer:{new_customer_email}\n==\n{self.email}")
