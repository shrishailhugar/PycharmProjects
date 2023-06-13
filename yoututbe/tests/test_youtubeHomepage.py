from PageObjects.YoutubeHomapage import YoutubeHomePage
from Utilities.Baseclass import BaseClass
from time import sleep

class TestyoutubeHomepage(BaseClass):
    def test_searchButton(self):
        logger=self.getLogger()
        homepageobj=YoutubeHomePage(self.driver)
        # homepageobj.getSearchBox().click()
        # homepageobj.getSearchBox().send_keys("savanahalli comedy kings")
        sleep(10)
        # homepageobj.getSearchBtn().click()

        homepageobj.getthumbnail().click()