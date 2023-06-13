from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
option=webdriver.ChromeOptions()
option.add_argument("headless")
service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj,options=option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
sleep(5)