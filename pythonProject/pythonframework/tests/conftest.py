import pytest
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:\\chromedriver.exe")
    option=webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    driver=webdriver.Chrome(service=service_obj,options=option)
    driver.implicitly_wait(5)
    driver.get("https://demo.guru99.com/test/radio.html")
    request.cls.driver=driver
    yield
    driver.close()
