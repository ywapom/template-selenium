from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class HomePage(BasePage):

    SIGNUP_BUTTON = (By.XPATH, "/html/body/route-view//home-element//main-layout/home-header/authstate-context[3]/signup-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def fsu(self):
        self.atry(self)

    def find_homepage_title(self):
        title = self.find_title()
        return title

    def click_sign_up(self):
        self.do_click(self.SIGNUP_BUTTON)
        self.wait(10)

    def get_url(self):
        return self.driver.url
