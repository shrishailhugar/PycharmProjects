from selenium.webdriver.common.by import By


class RadioB():
    webelement=(By.XPATH,"//div/input[@value='Option 1']")

    def __init__(self,driver):
        self.driver=driver

    def getwebelement(self):
        return self.driver.find_element(*RadioB.webelement)
