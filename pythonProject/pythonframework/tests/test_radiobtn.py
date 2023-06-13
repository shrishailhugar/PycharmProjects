import pytest

from pythonframework.PageObjects.RadioB import *
from pythonframework.PageObjects.Radiobuttonpage import Radiobuttonpage
from pythonframework.TestData.radiobtntestData import radioDataclass
from pythonframework.utilities.Basecalss import Baseclass
from time import sleep

class TestRadiobtn(Baseclass):

    # def test_in(self):
        # service_obj = Service("C:\\chromedriver.exe")
        # option=webdriver.ChromeOptions()
        # option.add_argument("--start-maximized")
        # driver=webdriver.Chrome(service=service_obj,options=option)
        # driver.get("https://demo.guru99.com/test/radio.html")
        # driver.find_element(By.XPATH,"//div/input[@value='Option 1']").click()
        # assert driver.find_element(By.XPATH,"//div/input[@value='Option
        # 1']").is_selected()==True

    def test_in(self,get_radiobutton_data):
        logger=self.getlogger()
        radiobt=Radiobuttonpage(self.driver)
        logger.error(get_radiobutton_data['radio'])
        radiobt.get_radionbtn(get_radiobutton_data['radio']).click()
        logger.info("the Radio Button clicked successfully")
        assert radiobt.get_radionbtn(get_radiobutton_data['radio']).is_selected()==True
        # assert radiobtnobj.get_radionbtn().is_selected==True
        sleep(2)
        self.driver.refresh()


    @pytest.fixture(params=radioDataclass.radiodata)
    def get_radiobutton_data(self,request):
        return request.param

