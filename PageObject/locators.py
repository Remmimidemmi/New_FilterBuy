from selenium.webdriver.common.by import By


class LoginPageLocators():
    SIGN_UP_EMAIL = (By.CSS_SELECTOR, "#signup-email")
    SIGN_UP_PASSWORD = (By.CSS_SELECTOR, "#signup-password")
    SIGN_UP_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#signup-confirm_password")
    FIRST_NAME = (By.CSS_SELECTOR, "#signup-first_name")
    LAST_NAME = (By.CSS_SELECTOR, "##signup-last_name")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#submit-signup")
