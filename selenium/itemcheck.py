from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from time import sleep

from selenium.webdriver.common.by import By

service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
sleep(5)
products=driver.find_elements(By.CSS_SELECTOR,"div[class='products'] div[class='product']")
print(len(products))
listp=['Cucumber','Raspberry','Strawberry']
j=0
for product in products:
    print(j)
    j+=1
    pname=product.find_element(By.CSS_SELECTOR,".product-name").text
    prname=pname.split()
    print(prname)
    assert prname[0] in listp
