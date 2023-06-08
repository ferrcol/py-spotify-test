from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class landingPage:

    URL = 'https://open.spotify.com/'

    LOGING_BUTTON  = (By.CSS_SELECTOR, 'button[data-testid="login-button"]')
    USER_AVATAR = (By.CSS_SELECTOR, '[data-testid="user-widget-avatar"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self):
        return self.browser.title
    
    def goToLoging(self):
        self.browser.find_element(*self.LOGING_BUTTON).click()

    def getUser(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.USER_AVATAR))

        return self.browser.find_element(*self.USER_AVATAR).get_attribute('title')
