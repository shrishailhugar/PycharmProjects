import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def SetUp(request):
    serviceobject=Service("C:\\chromedriver.exe")
    options=webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver=webdriver.Chrome(service=serviceobject,options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.youtube.com/results?search_query=savanahalli+comedy+kings")
    request.cls.driver=driver

    yield
    driver.close()