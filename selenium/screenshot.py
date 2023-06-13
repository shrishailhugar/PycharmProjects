from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=Service("C:\\Users\\ninga\\Downloads\\chromedriver_win32a\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight/2);")
driver.get_screenshot_as_file("screenshot2.png")