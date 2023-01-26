import random
import time


class Urls:
    REACT_MAIN_PAGE = "https://admin:admin!2@react.test.filterbuytest.com/"


class RegistrationCreds:
    REGISTRATION_EMAIL = "user_" + str(time.time()) + "@test.test"
    PASSWORD = "123"
    FIRST_NAME = "Test" + str(random.randint(1, 99999))
    LAST_NAME = "User_" + str(random.randint(1, 99999))


class LogInCreds:
    SIGN_IN_EMAIL = "test1@test.test"
    SIGN_IN_PASSWORD = "123"
