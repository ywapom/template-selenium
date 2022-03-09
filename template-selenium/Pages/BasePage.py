from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def sign_up(self):
        self.driver.get("")
        e = self.driver.find_element_by_tag_name("signup-button")
        print(e)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def find_title(self):
        return self.driver.title

    def wait(self, seconds):
        WebDriverWait(self.driver, seconds)

    def get_input_text(self, by_locator):
        text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).getAttribute("value")
        return text

    def get_text(self, by_locator):
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).getAttribute("innerHTML")
        return text

