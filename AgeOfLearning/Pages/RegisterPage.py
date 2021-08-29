from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class RegisterPage(BasePage):

    EMAIL_FIELD = (By.ID, "email")
    SUBMIT_BUTTON = (By.ID, "submit-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.REGISTER_URL)

    def enter_email(self, text):
        self.do_send_keys(self.EMAIL_FIELD, text)

    def find_register_title(self):
        title = self.find_title()
        return title

    def click_submit_button(self):
        self.do_click(self.SUBMIT_BUTTON)
        self.wait(10)

    def get_url(self):
        return self.driver.url

    def get_text_from_input(self):
        text = self.get_input_text(self.EMAIL_FIELD)
        return text
