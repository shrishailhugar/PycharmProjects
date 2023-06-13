from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep



service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/iframe")

# by default the driver not goin g to have access to frames

# provide id or name of frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"body[id='tinymce'] p").clear()

driver.find_element(By.CSS_SELECTOR,"body[id='tinymce'] p").send_keys(Keys.SHIFT+"hi all letters must be with capital letters")

# it's going to  switch back to original content which was loaded during


driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME,"h3").text)

sleep(5)