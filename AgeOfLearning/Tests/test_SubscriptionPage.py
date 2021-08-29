import pytest
from Tests.test_BaseTest import BaseTest
from Pages.SubscriptionPage import SubscriptionPage as SP



class TestSubscriptionPage(BaseTest):

    def test_for_become_a_member(self):
        self.SP = SP(self.driver)
        text = self.SP.get_become_text()
        assert text.lower() == "become a member!"
