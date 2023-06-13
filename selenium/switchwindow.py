from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()




# in which odrer the windows got opened in that order only they will be going to saved in list
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.find_element(By.LINK_TEXT,"Click Here").click()
# this must be written after opening new tab only
windowlist=driver.window_handles
driver.switch_to.window(windowlist[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
# here the driver going to close window[1]
driver.close()
driver.switch_to.window(windowlist[0])
print(driver.find_element(By.TAG_NAME,"h3").text)
sleep(5)

alert=driver.switch_to.alert
