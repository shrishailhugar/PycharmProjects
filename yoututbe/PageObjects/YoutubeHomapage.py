from selenium.webdriver.common.by import By


class YoutubeHomePage():
    searchbox=(By.CSS_SELECTOR,"input#search")
    searchbtn=(By.CSS_SELECTOR,"#search-icon-legacy")
    thumbnail=(By.CSS_SELECTOR,"//a[@id='thumbnail']")

    def __init__(self,driver):
        self.driver=driver


    def getSearchBox(self):
        return self.driver.find_element(*YoutubeHomePage.searchbox)

    def getSearchBtn(self):
        return self.driver.find_element(*YoutubeHomePage.searchbtn)

    def getthumbnail(self):
        return self.driver.find_element(*YoutubeHomePage.thumbnail)