import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:

    url = "http://www.linkedin.com"
    driver = webdriver.Chrome('/Users/Sho/Desktop/linkedin_test/chromedriver')
    longWait = 3
    shortWait = 1

    _ME_LINK = (By.ID, 'nav-settings__dropdown-trigger')
    _VIEW_PROFILE_BUTTON = (By.CLASS_NAME, 'button-tertiary-medium')
    _LOGOUT_BUTTON = (By.LINK_TEXT, 'Sign out')
    _HOME_LINK = (By.ID, 'feed-tab-icon')


    def goToHomePage(self):
        """
        Purpose: Navigate to homepage and return instance
        """

        homePageBtn = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._HOME_LINK))
        )

        homePageBtn.click()
        time.sleep(2)
        return self._returnInstance()


    def getTradeMark(self):
        """
        Purpose: Used as a static test method
        """

        spanList = self.driver.find_elements_by_tag_name('span')
        span = None

        for span in spanList:
            print(span)
            if span.text == 'LinkedIn Corporation © 2018':
                span = span

        if span is not None:
            return True

        # filteredSpans = list(filter(lambda span: span.text == 'LinkedIn Corporation © 2018', spanList))
        # print(filteredSpans)
        # if filteredSpans[0] is not None:
        #     return True


    def getPageUrl(self):

        time.sleep(1)
        return self.driver.current_url


    def _returnInstance(self):
        if "/feed/" in self.driver.current_url:
            print("URL: ", self.driver.current_url)
            print("Returning home instance")
            return Home()
        elif "/in/" in self.driver.current_url:
            print("URL: ", self.driver.current_url)
            print("Returning profile instance")
            return Profile()
        elif "/mynetwork/" or "/mynetwork/invite-sent/" or  "/search/results/" in self.driver.current_url:
            print("URL: ", self.driver.current_url)
            print("Returning network instance")
            return Network()
        elif "/search/results/" in self.driver.current_url:
            print("URL: ", self.driver.current_url)
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