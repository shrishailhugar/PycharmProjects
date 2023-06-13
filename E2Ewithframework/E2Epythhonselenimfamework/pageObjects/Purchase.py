from selenium.webdriver.common.by import By


class Purchase:
    country = (By.ID, "country")
    suggestion = (By.XPATH, "//a[.='India']")
    agreebtn = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchasebtn = (By.CSS_SELECTOR, ".btn-success")
    def __init__(self,driver):
        self.driver=driver


    def getCountry(self,cntr):
        return self.driver.find_element(*Purchase.country).send_keys(cntr)
    def getSuggestion(self):
        return  self.driver.find_element(*Purchase.suggestion)
    def getAgreebtn(self):
        return self.driver.find_element(*Purchase.agreebtn)
    def getsucbtn(self):
        return self.driver.find_element(*Purchase.purchasebtn)