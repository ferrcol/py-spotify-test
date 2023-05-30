from pages.landingpage import landingPage
from pages.loginpage import logingPage

   
def test_go_to_loging_page(browser):
    landing_page = landingPage(browser)
    loging_page = logingPage(browser)

    TITLE = 'Spotify'

    landing_page.load()

    assert TITLE in landing_page.title()
