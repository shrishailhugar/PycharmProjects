from selenium.webdriver.common.by import By


class Radiobuttonpage():

     radiobtn1=(By.XPATH,"//div/input[@value='Option 1']")
     radiobtn2 = (By.XPATH, "//div/input[@value='Option 2']")

     def __init__(self, driver):
         self.driver = driver



     def get_radionbtn(self,radiobtn):
        btn=radiobtn.split(" ")[1]
        if(btn=="1"):
         return self.driver.find_element(*self.radiobtn1)
        elif(btn=='2'):
            return self.driver.find_element(*self.radiobtn1)