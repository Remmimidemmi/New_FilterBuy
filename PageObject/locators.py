from selenium.webdriver.common.by import By


class MainPageLocators():
    MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#hdr-mr > span:nth-child(1) > a > i")
    HELLO_USERNAME = (By.CSS_SELECTOR, "#container > div.account-username > span")
    REQUEST_SALES_USER_FIELD = (By.CSS_SELECTOR, "#id_registration_info")
    BECOME_SALES_USER_BUTTON = (By.CSS_SELECTOR, "button.btn")
    SALES_LINK_TAB = (By.CSS_SELECTOR, "#outside-sales > div:nth-child(1)")
    USER_MY_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#hdr-mr > span:nth-child(1) > span:nth-child(1)")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#account-drop-logout > a")


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


class ReactAdminLocators():
    SIGN_IN_EMAIL = (By.CSS_SELECTOR, "#id_username")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "#id_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#bottombar > button:nth-child(1)")
    FIRST_CHECKBOX_ACTIVE = (By.CSS_SELECTOR, "#id_form-0-active")
    SAVE_BUTTON = (By.CSS_SELECTOR, "#bottombar > button")
