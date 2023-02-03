import random
import time


class RegistrationCreds:
    REGISTRATION_EMAIL = "user_" + str(time.time()) + "@test.test"
    PASSWORD = "123"
    FIRST_NAME = "Test" + str(random.randint(1, 99999))
    LAST_NAME = "User_" + str(random.randint(1, 99999))


class LogInCreds:
    SIGN_IN_EMAIL = "test1@test.test"
    SIGN_IN_EMAIL_SALES = "user_1675172463.5326242@test.test"
    SIGN_IN_REAL_EMAIL = "zast0tsaz@gmail.com"
    SIGN_IN_PASSWORD = "123"
    SIGN_IN_EMAIL_INCORRECT = "test0@test.test"
    SIGN_IN_PASSWORD_INCORRECT = "1234"


class AdminCreds:
    REACT_ADMIN = "vlad.sh+admin@core-tech.ru"


class NewCustomerData:
    BUSINESS_NAME = "PoguCo" + str(random.randint(1, 99999))
