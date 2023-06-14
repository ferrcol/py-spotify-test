import pytest
import re
import os

py_user = os.environ.get('PY_user')
py_pass = os.environ.get('PY_pass')

class TestClassPlayList:
    def test_should_create_list_successfully(self, landing_page, login_page):
        landing_page.load()
        landing_page.goToLoging()
        login_page.doLogin(py_user,py_pass)
        landing_page.createList()

        assert landing_page.getFirstPlaylistName() == 'My Playlist #2'

        landing_page.deleteList()
        
    #def test_should_delete_playlist_successfully(self, landing_page, login_page):
        