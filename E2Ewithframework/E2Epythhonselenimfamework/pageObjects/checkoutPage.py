from selenium.webdriver.common.by import By


class checkoutPage:
    card_id = (By.CSS_SELECTOR, ".card")
    cardas=(By.CSS_SELECTOR,"div[class='card-body'] h4 a")
    mobwebele=(By.CSS_SELECTOR,".card-footer button")
    checkbtn=(By.CSS_SELECTOR,".btn-primary")
    okbtn=(By.CSS_SELECTOR,".btn-success")
    def __init__(self,driver):
        self.driver=driver


    def getCardTitles(self):
        return self.driver.find_elements(*checkoutPage.card_id)
    def getcard(self,mob):
        return mob.find_element(*checkoutPage.cardas).text
    def getmob(self):
        return self.driver.find_element(*checkoutPage.mobwebele)
    def getcheckbtn(self):
        return self.driver.find_element(*checkoutPage.checkbtn)
    def get_okbtn(self):
        return self.driver.find_element(*checkoutPage.okbtn)
