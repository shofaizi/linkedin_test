import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:

    url = "http://www.linkedin.com"
    driver = webdriver.Chrome('/Users/Sho/Desktop/linkedin_test/chromedriver')
    longWait = 5
    shortWait = 1

    _ME_LINK = (By.ID, 'nav-settings__dropdown-trigger')
    _VIEW_PROFILE_BUTTON = (By.CLASS_NAME, 'button-tertiary-medium')
    _LOGOUT_BUTTON = (By.LINK_TEXT, 'Sign out')


    def _returnInstance(self):

        if "/feed/" in self.driver.current_url:
            print("Returning home instance")
            return Home()
        elif "/mynetwork/" in self.driver.current_url:
            print("Returning network instance")
            return Network()
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


    def expandProfileNavigator(self):

        meButton = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._ME_LINK))
        )

        meButton.click()
        time.sleep(1)


    def openOwnProfile(self):

        viewProfileButton = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._VIEW_PROFILE_BUTTON))
        )

        viewProfileButton.click()

        return Profile()


    def logOut(self):

        self.expandProfileNavigator()

        logoutButton = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._LOGOUT_BUTTON))
        )

        logoutButton.click()

        self.tearDown()


from pages.network import Network
from pages.home import Home
from pages.profile import Profile
from pages.result import Result