from selenium.webdriver.common.by import By

class landingPage:

    URL = 'https://open.spotify.com/'

    LOGING_BUTTON  = (By.CSS_SELECTOR, 'button[data-testid="login-button"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self):
        return self.browser.title