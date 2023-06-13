import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setUp")
class BaseClass:

    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        print("Logger_name=",loggerName)
        logger=logging.getLogger(loggerName)
        filehandler=logging.FileHandler("LogFile.log")
        formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self,text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, text)))

    def selectOptionByText(self,text,locator):
        sel=Select(locator)
        sel.select_by_visible_text(text)