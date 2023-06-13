from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
service_obj=Service("C:\\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("headless")

driver=webdriver.Chrome(service=service_obj,options=options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

sleep(5)