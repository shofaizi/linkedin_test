from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Base:

    url = "http://www.linkedin.com"
    driver = webdriver.Chrome('/Users/Sho/Desktop/linkedin_test/chromedriver')
    longWait = 3
    shortWait = 1


    def _returnInstance(self):

        if "/feed/" in self.driver.current_url:
            print("Returning home instance")
            return Home()
        elif "/mynetwork/" in self.driver.current_url:
            print("Returning network instance")
            return Network()
        elif "/jobs/" in self.driver.current_url:
            print("Returning jobs instance")
            return Job()
        elif "/messaging/" in self.driver.current_url:
            print("Returning messaging instance")
            return Messaging()
        elif "/in/" in self.driver.current_url:
            print("Returning profile instance")
            return Profile()
        elif "/search/results/" in self.driver.current_url:
            print("Returning result instance")
            return Result()


    def _sendKeys(self, element, value):

        element.clear()
        element.send_keys(value)
        element.send_keys(Keys.RETURN)


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


from messaging import Messaging
from network import Network
from job import Job
from home import Home
from profile import Profile
from result import Result