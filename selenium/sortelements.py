from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

dropdown=Select(driver.find_element(By.CSS_SELECTOR,"#page-menu"))
dropdown.select_by_index(2)
driver.find_element(By.XPATH,"//th/span[text()='Veg/fruit name']").click()
veglist=driver.find_elements(By.XPATH,"//tr/td[1]")
vegnames=[x.text for x in veglist ]
for veg in veglist:
    print(veg.text)

print(vegnames)

sortedvegnames=sorted(vegnames,reverse=True)
print(sortedvegnames)
driver.find_element(By.XPATH,"//th/span[text()='Veg/fruit name']").click()
veglista=driver.find_elements(By.XPATH,"//tr/td[1]")
clicksortlist=[x.text for x in veglista]
print(clicksortlist)
assert sortedvegnames==clicksortlist