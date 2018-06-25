from selenium.webdriver.common.by import By
from pages.base import Base
import time


class Home(Base):

    _BUTTON_PROFILE = (By.ID, 'nav-settings__dropdown-trigger')
    _VIEW_PROFILE = (By.CLASS_NAME, 'button-tertiary-medium')
    _BUTTONS = (By.TAG_NAME, 'button')
    _DIVS = (By.TAG_NAME, 'div')
    _INPUTS = (By.TAG_NAME, 'input')


    def searchUser(self, value):

        inputFields = self.driver.find_elements(*self._INPUTS)
        self._sendKeys(inputFields[0], value)

        return Result()


    def sharePost(self, value):
        """
        Purpose:
            Will locate the input field and enter values and share the post.
        """

        buttonList = self.driver.find_elements(*self._BUTTONS)
        postField = None

        for button in buttonList:
            if button.text == 'Share an article, photo, video or idea':
                postField = button

        assert postField is not None
        postField.click()
        time.sleep(1)

        divList = self.driver.find_elements(*self._DIVS)
        divList = list(filter(lambda div: div.get_attribute('role') == 'textbox', divList))
        divList[0].click()
        divList[0].send_keys(value)

        time.sleep(1)

        buttonList = self.driver.find_elements(*self._BUTTONS)

        for button in buttonList:
            if button.text == "Post":
                button.click()
                time.sleep(1)
                return self.driver.refresh()


from pages.result import Result
