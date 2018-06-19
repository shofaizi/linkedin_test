from base import Base
from selenium.webdriver.common.by import By
from profile import Profile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


class Home(Base):

    _SEARCH_INPUT = (By.ID, 'ember1489')
    _BUTTON_NETWORK = (By.LINK_TEXT, 'mynetwork')
    _BUTTON_MESSAGING = (By.LINK_TEXT, "messaging")
    _BUTTON_JOBS = (By.LINK_TEXT, 'jobs')
    _BUTTON_PROFILE = (By.ID, 'nav-settings__dropdown-trigger')
    _VIEW_PROFILE = (By.CLASS_NAME, 'button-tertiary-medium')
    _BUTTON_CONNECT = (By.XPATH, '//*[@id="ember4172"]/div')
    _BUTTON_NOTE = (By.CLASS_NAME, 'mr1')
    _BUTTON_SEND_INVITE = (By.CLASS_NAME, 'ml1')
    _NOTE_FIELD = (By.NAME, 'message')


    def searchUser(self, value):

        inputFields = self.driver.find_elements(By.TAG_NAME, 'input')

        self._sendKeys(inputFields[0], value)
        return Result()


    # def connectUser(self, value):
    #
    #     time.sleep(3)
    #
    #     userLink = self.driver.find_element_by_class_name('search-result__result-link')
    #     userLink.click()
    #     return Profile()


    # def submitLogin(self):
    #     self._clickSubmit((self._LOGIN_SUBMIT))
    #     return self._returnInstance()


from result import Result