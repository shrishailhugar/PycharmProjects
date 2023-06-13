import pytest

from E2Epythhonselenimfamework.testData.HomepageTestData import HomePageTestData
from E2Epythhonselenimfamework.utilities.BaseClass import BaseClass
from E2Epythhonselenimfamework.pageObjects.HomePage import HomePage
from time import sleep

class TestHomepage(BaseClass):
    def test_forSubmission(self,getData):
        log=self.getLogger()
        homepage=HomePage(self.driver)
        homepage.getName().send_keys(getData["name"])
        log.info(getData["name"]+" added succesfully")
        log.debug("added succesfully")
        homepage.gerEmail().send_keys(getData["email"])
        homepage.getpassword().send_keys(["password"])
        homepage.getCheckBox().click()
        self.selectOptionByText("Male",homepage.getDropdown())
        homepage.getradiobtn().click()
        homepage.getdate().send_keys(getData["DOB"])
        sleep(5)
        homepage.scroll()
        homepage.getsubmitbtn().click()

        assert "Success!" ==homepage.getSuccess().text
        self.driver.refresh()

    # @pytest.fixture(params=[{"name":"Bapu","email":"bapuraya@gmail.com","password":"Bapu@123","DOB":"10/10/2008"},{"name":"Guru","email":"asmakam@gmail.com","password":"asmakam@123","DOB":"10/10/2008"}])
    # def getData(self,request):
    #     return request.param

    @pytest.fixture(
        params=HomePageTestData.users_info)
    def getData(self, request):
        print("request=",request.param)
        return request.param
