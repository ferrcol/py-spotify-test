from pages.landingpage import landingPage
from pages.loginpage import logingPage
from selenium.webdriver.common.by import By

import os
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

py_user = os.environ.get('PY_user')
py_pass = os.environ.get('PY_pass')

   
def test_go_to_loging_page(browser):
    landing_page = landingPage(browser)
    loging_page = logingPage(browser)

    TITLE1 = 'Spotify - Web Player: Music for everyone'

    TITLE2 = 'Login'

    USER_FIELD = (By.ID, 'login-username')
    PASS_FIELD = (By.ID, 'login-password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    USER_AVATAR = (By.CSS_SELECTOR, '[data-testid="user-widget-avatar"]')

    landing_page.load()


    assert TITLE1 in landing_page.title()

    landing_page.goToLoging()

    wait = WebDriverWait(browser, 10)
    wait.until(EC.title_contains(TITLE2))

    assert TITLE2 in loging_page.title()

    wait.until(EC.visibility_of_element_located(USER_FIELD))

    browser.find_element(*USER_FIELD).send_keys(py_user)

    wait.until(EC.visibility_of_element_located(PASS_FIELD))

    browser.find_element(*PASS_FIELD).send_keys(py_pass)

    browser.find_element(*LOGIN_BUTTON).click()

    wait.until(EC.visibility_of_element_located(USER_AVATAR))

    assert browser.find_element(*USER_AVATAR).get_attribute('title') == py_user








