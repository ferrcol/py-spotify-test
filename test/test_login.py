
import pytest

import os

py_user = os.environ.get('PY_user')
py_pass = os.environ.get('PY_pass')

class TestClassLogin:
    def test_should_show_an_error_for_wrong_user(self, clean, landing_page, login_page):
        landing_page.load()
        landing_page.goToLoging()
        login_page.doLogin('fer',py_pass)

        assert login_page.getMge() == "Error:Incorrect username or password."

    def test_should_login_with_valid_credentials(self, clean, landing_page, login_page):
        landing_page.load()
        landing_page.goToLoging()
        login_page.doLogin(py_user,py_pass)

        assert landing_page.getUser() == py_user










