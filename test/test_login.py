import pytest
import os

py_user = os.environ.get('PY_user')
py_pass = os.environ.get('PY_pass')

class TestClassLogin:
    def test_should_login_with_valid_credentials(self, clean, landing_page, login_page):
        landing_page.load()
        landing_page.goToLoging()
        login_page.doLogin(py_user,py_pass)

        assert landing_page.getUser() == py_user

    def test_should_show_an_error_for_wrong_user(self, clean, landing_page, login_page):
        landing_page.load()
        landing_page.goToLoging()
        login_page.doLogin('wrong',py_pass)

        assert login_page.getMge() == "Error:Incorrect username or password."

    def test_should_show_an_error_for_wrong_pass(self, clean, landing_page, login_page):
        landing_page.load()
        landing_page.goToLoging()
        login_page.doLogin(py_user,'wrong')

        assert login_page.getMge() == "Error:Incorrect username or password."

    def test_should_show_an_error_for_empty_fields(self, clean, landing_page, login_page):
        landing_page.load()
        landing_page.goToLoging()
        login_page.doLogin('','')

        assert login_page.getMge() == "Error:Incorrect username or password."

    def test_should_show_a_message_for_successful_password_reset(self, clean, landing_page, login_page, reset_page):
        landing_page.load()
        landing_page.goToLoging()
        login_page.goToResetPassPage()
        reset_page.doResetPass('wrong')

        assert reset_page.getMge() == "Password Reset"











