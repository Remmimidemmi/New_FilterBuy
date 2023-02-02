import random
import time


class Urls:
    ADMIN_REACT_PAGE = "https://admin:admin!2@react.test.filterbuytest.com/admin/"
    ADMIN_OUTSIDE_USERS = "https://react.test.filterbuytest.com/admin/customer/outsidesalesuser/"

    REACT_MAIN_PAGE = "https://admin:admin!2@react.test.filterbuytest.com/"
    REACT_REQUEST_NEW_SALES_USER = "https://admin:admin!2@react.test.filterbuytest.com/outside-sales/registration/"

    REAL_EMAIL_URL = "https://www.google.com/gmail/about/"


class RegistrationCreds:
    REGISTRATION_EMAIL = "user_" + str(time.time()) + "@test.test"
    PASSWORD = "123"
    FIRST_NAME = "Test" + str(random.randint(1, 99999))
    LAST_NAME = "User_" + str(random.randint(1, 99999))


class LogInCreds:
    SIGN_IN_EMAIL = "test1@test.test"
    SIGN_IN_REAL_EMAIL = "zast0tsaz@gmail.com"
    SIGN_IN_PASSWORD = "123"
    SIGN_IN_EMAIL_INCORRECT = "test0@test.test"
    SIGN_IN_PASSWORD_INCORRECT = "1234"



class AdminCreds:
    REACT_ADMIN = "vlad.sh+admin@core-tech.ru"
