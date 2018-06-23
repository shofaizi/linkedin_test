from selenium.webdriver.common.by import By
from pages.base import Base
import time
from selenium.webdriver.support import expected_conditions as EC


class Home(Base):

    _SEARCH_INPUT = (By.ID, 'ember1489')
    _BUTTON_NETWORK = (By.LINK_TEXT, 'mynetwork')
    _BUTTON_MESSAGING = (By.LINK_TEXT, "messaging")
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


    def getPageUrl(self):

        return self.driver.current_url


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


    def sharePost(self, value):
        """
        Purpose:
            Will locate the input field and enter values and share the post.
        """

        buttonList = self.driver.find_elements_by_tag_name('button')
        postField = None

        for button in buttonList:
            if button.text == 'Share an article, photo, video or idea':
                postField = button

        postField.click()
        time.sleep(1)

        divList = self.driver.find_elements_by_tag_name('div')
        divList = list(filter(lambda div: div.get_attribute('role') == 'textbox', divList))
        divList[0].click()
        divList[0].send_keys(value)

        time.sleep(1)

        buttonList = self.driver.find_elements_by_tag_name('button')

        for button in buttonList:
            if button.text == "Post":
                button.click()
                self.driver.refresh()


from pages.result import Result
