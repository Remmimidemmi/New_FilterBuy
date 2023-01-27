import random
import time


class Urls:
    ADMIN_REACT_PAGE = "https://admin:admin!2@react.test.filterbuytest.com/admin/"
    ADMIN_OUTSIDE_USERS = "https://react.test.filterbuytest.com/admin/customer/outsidesalesuser/"

    REACT_MAIN_PAGE = "https://admin:admin!2@react.test.filterbuytest.com/"
    REACT_REQUEST_NEW_SALES_USER = "https://admin:admin!2@react.test.filterbuytest.com/outside-sales/registration/"


class RegistrationCreds:
    REGISTRATION_EMAIL = "user_" + str(time.time()) + "@test.test"
    PASSWORD = "123"
    FIRST_NAME = "Test" + str(random.randint(1, 99999))
    LAST_NAME = "User_" + str(random.randint(1, 99999))


class LogInCreds:
    SIGN_IN_EMAIL = "test1@test.test"
    SIGN_IN_PASSWORD = "123"

class AdminCreds:
    REACT_ADMIN = "vlad.sh+admin@core-tech.ru"

