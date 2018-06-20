from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Base:

    url = "http://www.linkedin.com"
    driver = webdriver.Chrome('/Users/Sho/Desktop/linkedin_test/chromedriver')
    longWait = 3
    shortWait = 1

    _ME_LINK = (By.ID, 'nav-settings__dropdown-trigger')
    _VIEW_PROFILE_BUTTON = (By.CLASS_NAME, 'button-tertiary-medium')


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


    def open_ownProfile(self):

        meButton = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._ME_LINK))
        )

        meButton.click()
        time.sleep(1)

        viewProfileButton = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._VIEW_PROFILE_BUTTON))
        )

        viewProfileButton.click()

        return Profile()


from messaging import Messaging
from network import Network
from job import Job
from home import Home
from profile import Profile
from result import Result