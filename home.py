from base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(Base):

    SEARCH_INPUT = (By.ID, 'ember1489')
    BUTTON_NETWORK = (By.LINK_TEXT, 'mynetwork')
    BUTTON_MESSAGING = (By.LINK_TEXT, "messaging")
    BUTTON_JOBS = (By.LINK_TEXT, 'jobs')
    BUTTON_PROFILE = (By.ID, 'nav-settings__dropdown-trigger')
    VIEW_PROFILE = (By.CLASS_NAME, 'button-tertiary-medium')



    def searchUser(self, value):

        inputFields = self.driver.find_elements(By.TAG_NAME, 'input')

        self._sendKeys(inputFields[0], value)
        return self._returnInstance()

