from selenium.webdriver.common.by import By

class logingPage:

    URL = 'https://accounts.spotify.com/en/login'

    LOGING_DIV  = (By.CSS_SELECTOR, 'div[data-testid="login-container"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)