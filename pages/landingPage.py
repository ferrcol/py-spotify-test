from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class landingPage:

    URL = 'https://open.spotify.com/'

    LOGING_BUTTON  = (By.CSS_SELECTOR, 'button[data-testid="login-button"]')
    USER_AVATAR = (By.CSS_SELECTOR, '[data-testid="user-widget-avatar"]')
    LIST_CREATE_PLAYLIST_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Create playlist or folder"]')
    CREATE_PLAYLIST_BUTTON = (By.CSS_SELECTOR, '#context-menu button')
    NEW_PLAYLIST_ELEMENT = (By.CSS_SELECTOR, '[id^="listrow-title-spotify:playlist:"]')
    MORE_OPTIONS_BUTTON = (By.CSS_SELECTOR,'[data-testid="more-button"]')
    CONTEXT_MENU = (By.CSS_SELECTOR,'#context-menu button') 
    DELETE_BUTTON =  (By.CSS_SELECTOR, 'button[aria-label^="Delete "]')

   

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def title(self):
        return self.browser.title
    
    def goToLoging(self):
        self.browser.find_element(*self.LOGING_BUTTON).click()

    def createList(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.LIST_CREATE_PLAYLIST_BUTTON))
        self.browser.find_element(*self.LIST_CREATE_PLAYLIST_BUTTON).click()
        wait.until(EC.visibility_of_element_located(self.CREATE_PLAYLIST_BUTTON))
        self.browser.find_elements(*self.CREATE_PLAYLIST_BUTTON)[0].click()
        time.sleep(2)
        wait.until(EC.visibility_of_element_located(self.NEW_PLAYLIST_ELEMENT))

    def deleteList(self):
        wait = WebDriverWait(self.browser, 10)
        #wait.until(EC.visibility_of_element_located(self.NEW_PLAYLIST_ELEMENT))
        #self.browser.find_element(*self.NEW_PLAYLIST_ELEMENT).click()
        wait.until(EC.visibility_of_element_located(self.MORE_OPTIONS_BUTTON))
        self.browser.find_element(*self.MORE_OPTIONS_BUTTON).click()
        wait.until(EC.visibility_of_element_located(self.CONTEXT_MENU))
        self.browser.find_elements(*self.CONTEXT_MENU)[3].click()
        wait.until(EC.visibility_of_element_located(self.DELETE_BUTTON))
        self.browser.find_element(*self.DELETE_BUTTON).click()



    def getUser(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.USER_AVATAR))

        return self.browser.find_element(*self.USER_AVATAR).text
    

    def getFirstPlaylistName(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.NEW_PLAYLIST_ELEMENT))

        return self.browser.find_elements(*self.NEW_PLAYLIST_ELEMENT)[0].text
