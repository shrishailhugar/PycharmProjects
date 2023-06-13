from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

# implicit wait waits until mentioned seconds it doesnn't mean it will wait for max seconds in case if the object loads within 2 sec then it will proceed where it's going to save 3 sec compared to sleep
driver.implicitly_wait(5) #it's a gloabal time out'

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")

# for below line the implicit wait may not work because it's plural and it's expecting list
# if it returns empty-list(where still all list elements not loaded) implicit wait stops thinking i got list eventhough it's empty bcz impwait just waiting for list it's not going to worry about all list elements

products=driver.find_elements(By.CSS_SELECTOR,"div[class='product']")

for prouct in products:
    name=prouct.find_element(By.CSS_SELECTOR,"h4").text
    if "Cucumber" in name:
        prouct.find_element(By.CSS_SELECTOR,"div a[class='increment']").click()
        # sleep(2)
        prouct.find_element(By.CSS_SELECTOR,"div a[class='increment']").click()
        # sleep(1)
        prouct.find_element(By.CSS_SELECTOR,"div button").click()
    if "Strawberry" in name:
        prouct.find_element(By.CSS_SELECTOR,"div a[class='increment']").click()
        prouct.find_element(By.CSS_SELECTOR, "div button").click()
        # sleep(2)
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
# sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# sleep(2)
driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promobtn").click()
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)

driver.find_element(By.XPATH,"//button[contains(text(),'Order') ]").click()
# sleep(6)
dropdown=Select(driver.find_element(By.CSS_SELECTOR,"select"))
dropdown.select_by_visible_text("India")
driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Proc')]").click()
sleep(5)