"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver
from pages.landingPage import landingPage
from pages.loginPage import loginPage


@pytest.fixture(scope="class")
def browser():

  # Initialize the ChromeDriver instance
  b = selenium.webdriver.Chrome()

  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()

@pytest.fixture(scope="class")
def landing_page(browser):
    return landingPage(browser)

@pytest.fixture(scope="class")
def login_page(browser):
    return loginPage(browser)

@pytest.fixture
def clean(browser):
    browser.execute_cdp_cmd('Storage.clearDataForOrigin', {
        "origin": '*',
        "storageTypes": 'all',
    })
