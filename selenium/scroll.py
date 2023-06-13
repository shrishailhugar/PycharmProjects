from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")

# here selenium dont have any options to scroll so
# it will execute javascript which user going to provide
#don't forget :(colon)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot1.png")
