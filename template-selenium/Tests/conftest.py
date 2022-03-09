import pytest
from selenium import webdriver
from Config.config import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    #if request.param == "firefox":
    #   web_driver = webdriver.Firefox(TestData.FIREFOX_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()