from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class resetPage:
    URL = 'https://accounts.spotify.com/en/password-reset'

    USER_INPUT = (By.CSS_SELECTOR, "input#email_or_username")
    SEND_BUTTON = (By.CSS_SELECTOR, "button.Button-qlcn5g-0")
    HEAD_DIV = (By.CSS_SELECTOR, '[class*="PageHeading"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self):
        return self.browser.title
    
    def doResetPass(self,username):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.USER_INPUT))
        self.browser.find_element(*self.USER_INPUT).send_keys(username)
        self.browser.find_element(*self.SEND_BUTTON).click()

    def getMge(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.HEAD_DIV))
        return self.browser.find_element(*self.HEAD_DIV).get_attribute("textContent")