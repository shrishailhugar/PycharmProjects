from selenium.webdriver.common.by import By

from E2Epythhonselenimfamework.pageObjects.checkoutPage import checkoutPage


class HomePage:
    shop=(By.LINK_TEXT, "Shop")
    name=(By.CSS_SELECTOR,"[name='name']")
    email=(By.CSS_SELECTOR,"[name='email']")
    password=(By.CSS_SELECTOR,"[type='password']")
    seldropdown=(By.ID,"exampleFormControlSelect1")
    date=(By.NAME,"bday")
    submit=(By.CSS_SELECTOR,"[type='submit']")
    radio=(By.ID,"inlineRadio2")
    suceess=(By.CSS_SELECTOR,".alert-success strong")

    check=(By.ID,"exampleCheck1")
    def __init__(self,driver):
        self.driver=driver
    def shopItem(self):
        print(self.driver.find_element(*HomePage.shop))
        # * to deserialize
        (self.driver.find_element(*HomePage.shop)).click()
        return checkoutPage(self.driver)
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def gerEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.seldropdown)

    def getdate(self):
        return self.driver.find_element(*HomePage.date)

    def getsubmitbtn(self):
        return  self.driver.find_element(*HomePage.submit)

    def getradiobtn(self):
        return self.driver.find_element(*HomePage.radio)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.suceess)
    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight/2);")