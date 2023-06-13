import pytest
from selenium.webdriver.common.by import By
from time import sleep


from selenium.webdriver.support.wait import WebDriverWait

from E2Epythhonselenimfamework.pageObjects.HomePage import HomePage
from E2Epythhonselenimfamework.pageObjects.Purchase import Purchase
from E2Epythhonselenimfamework.pageObjects.checkoutPage import checkoutPage
from E2Epythhonselenimfamework.utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setUp")-- it's not needed now as we are inheriting BaseClass for fixtures.
class Test_class(BaseClass):
    def test_firstfun(self):
        #         getting driver by self  which we get from setup bcz it's now  class attribute we can call it by self or by classname
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        homepage = HomePage(self.driver)
        # homepage.shopItem().click()
        # checkoutpage = checkoutPage(self.driver)
        # optimizing by getting next page object from the current page
        checkoutpage=homepage.shopItem()
        mobitems = checkoutpage.getCardTitles()
        for mob in mobitems:
            text = checkoutpage.getcard(mob)
            print(text)
            if text == "Nokia Edge":
                checkoutpage.getmob().click()
        checkoutpage.getcheckbtn().click()
        checkoutpage.get_okbtn().click()
        p=Purchase(self.driver)
        p.getCountry("india")
        self.verifyLinkPresence("//a[.='India']")
        sleep(10)

        p.getSuggestion().click()
        p.getAgreebtn().click()
        p.getsucbtn().click()

        sleep(5)
