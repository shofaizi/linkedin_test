from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Base:

    url = "http://www.linkedin.com"
    driver = webdriver.Chrome('/Users/Sho/Desktop/linkedin_test/chromedriver')
    longWait = 5
    shortWait = 1


    def _sendKeys(self, element, value):

        element.clear()
        element.send_keys(value)
        element.send_keys(Keys.TAB)


    def _clickSubmit(self, element):

        element.click()


    def setUp(self):

        print("Opening :", self.url)
        self.driver.get(self.url)
        self.driver.maximize_window()


    def tearDown(self):

        self.driver.close()
        print("Closing driver now...")
        self.driver.quit()
