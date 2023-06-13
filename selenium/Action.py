from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep

# need to add performm at the end
from selenium.webdriver.common.by import By

service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
action=ActionChains(driver)
# Hower
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform() #perform must be there for action at the the end
action.move_to_element(driver.find_element(By.Id))
#right-click
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

# click
action.click(driver.find_element(By.LINK_TEXT,"Reload")).perform()



sleep(5)