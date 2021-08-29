import pytest
from Tests.test_BaseTest import BaseTest
from Pages.HomePage import HomePage as HP
from Config.config import TestData


class TestHomePage(BaseTest):

    def test_sign_up_click(self):
        self.HP = HP(self.driver)
        self.HP.click_sign_up()
        new_url = HP.get_url()
        assert new_url == "https://www.abcmouse.com/abc/prospect-register/"

    def test_find_title(self):
        self.HP = HP(self.driver)
        title = self.HP.find_homepage_title()
        print(title)
        assert "ABCmouse" in title
