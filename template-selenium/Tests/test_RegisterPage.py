import pytest
from Tests.test_BaseTest import BaseTest
from Pages.RegisterPage import RegisterPage as RP
from Config.config import TestData


class TestRegisterPage(BaseTest):

    @pytest.mark.run(order=1)
    def test_good_email(self):
        self.RP = RP(self.driver)
        self.RP.enter_email(TestData.EMAIL)
        text = self.RP.get_text_from_input()
        assert text == TestData.EMAIL

    @pytest.mark.run(order=2)
    def test_submit_email(self):
        self.RP = RP(self.driver)
        self.RP.click_submit_button()
        new_url = RP.get_url()
        assert new_url == "https://www.abcmouse.com/abt/subscription"
