from selenium.webdriver.common.by import By


class MainPageLocators():
    MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#hdr-mr > span:nth-child(1) > a > i")
    HELLO_USERNAME = (By.CSS_SELECTOR, "#container > div.account-username > span")


class LoginPageLocators():
    SIGN_UP_EMAIL = (By.CSS_SELECTOR, "#signup-email")
    SIGN_UP_PASSWORD = (By.CSS_SELECTOR, "#signup-password")
    SIGN_UP_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#signup-confirm_password")
    FIRST_NAME = (By.CSS_SELECTOR, "#signup-first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#signup-last_name")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#submit-signup")
    SiGN_IN_EMAIL = (By.CSS_SELECTOR, "#login-email")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "#login-password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#submit-login")