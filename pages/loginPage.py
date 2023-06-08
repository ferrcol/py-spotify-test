from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class loginPage:

    URL = 'https://accounts.spotify.com/en/login'

    LOGING_DIV  = (By.CSS_SELECTOR, 'div[data-testid="login-container"]')
    USER_FIELD = (By.ID, 'login-username')
    PASS_FIELD = (By.ID, 'login-password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    BANNER = (By.CSS_SELECTOR, '[data-encore-id="banner"]')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self):
        return self.browser.title
    
    def doLogin(self, py_user,py_pass):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.USER_FIELD))
        self.browser.find_element(*self.USER_FIELD).send_keys(py_user)
        wait.until(EC.visibility_of_element_located(self.PASS_FIELD))
        self.browser.find_element(*self.PASS_FIELD).send_keys(py_pass)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def getMge(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.BANNER))
        return self.browser.find_element(*self.BANNER).get_attribute("textContent")