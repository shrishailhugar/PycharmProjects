from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("C:\\chromedriver.exe")
option=webdriver.ChromeOptions()
option.add_argument("--start-maximized")
driver=webdriver.Chrome(service=service_obj,options=option)
driver.implicitly_wait(2)
wait=WebDriverWait(driver,8)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight/2);")
mobitems=driver.find_elements(By.CSS_SELECTOR,".card")

for mob in mobitems:
    text=mob.find_element(By.CSS_SELECTOR,"div[class='card-body'] h4 a").text
    print(text)
    if text=="Nokia Edge":
        mob.find_element(By.CSS_SELECTOR,".card-footer button").click()

driver.find_element(By.CSS_SELECTOR,".btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
driver.find_element(By.ID,"country").send_keys("india")
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".suggestions a")))
driver.find_element(By.CSS_SELECTOR,".suggestions a").click()
driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".alert-success strong")))
assert "Success!"==driver.find_element(By.CSS_SELECTOR,".alert-success strong").text
sleep(5)