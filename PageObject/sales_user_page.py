import time

from selenium.webdriver.common.keys import Keys

from .URLs import Urls
from .base_page import BasePage
from .data import NewCustomerData, RegistrationCreds
from .locators import NewCustomersLocators, MainPageLocators


class SalesUserPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.email = RegistrationCreds.REGISTRATION_EMAIL

    def go_to_customers_tab(self):
        self.browser.find_element(*NewCustomersLocators.CUSTOMERS_TAB).click()

    def go_to_mask_user(self):
        self.go_to_customers_tab()
        user = self.browser.find_element(
            *NewCustomersLocators.CUSTOMERS_LIST_NEW_CUSTOMER).text.split('@')[0]
        self.browser.find_element(*NewCustomersLocators.MASK_BUTTON).click()
        user_to_mask = self.browser.find_element(
            *NewCustomersLocators.HELLO_BUSINESS_USER_TEXT).text[7:-1]
        current_link = self.browser.current_url
        assert user_to_mask == user \
               and current_link == Urls.REACT_MASK_BUSINESS_USER, \
            f"Mask unsuccessful!\nUser to mask:\n{user_to_mask}\nUser:\n{user}\nLink:\n{current_link}"
        print(f"Redirect on link:\n{current_link}\nto mask business user:\n{user}!")

    def go_to_customer_details(self):
        self.go_to_customers_tab()
        user_to_details = self.browser.find_element(*NewCustomersLocators.CUSTOMERS_LIST_CUSTOMER_NAME).text
        self.browser.find_element(*NewCustomersLocators.CUSTOMER_DETAILS_BUTTON).click()
        user_from_details = self.browser.find_element(*NewCustomersLocators.USER_NAME_FROM_DETAILS).text
        customer_information = self.browser.find_element(*NewCustomersLocators.CUSTOMER_INFORMATION_INSCR).text
        assert user_to_details == user_from_details, f"Details button doesn't work correctly!" \
                                                     f"\n{user_from_details}\n!=\n{user_to_details}"
        print(f"Details button work correctly:\n{customer_information}\n{user_to_details} == {user_from_details}")

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
