from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class SubscriptionPage(BasePage):

    BECOME = (By.CLASS_NAME, "page-tag")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.SUBSCRIBE_URL)

    def get_become_text(self):
        text = self.get_text(self.BECOME)
        return text

    def find_subscription_title(self):
        title = self.find_title()
        return title

    def get_url(self):
        return self.driver.url
