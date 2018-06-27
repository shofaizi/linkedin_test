import time
from pages.base import Base
from pages.profile import Profile
from selenium.webdriver.common.by import By


class Network(Base):

    _SPANS = (By.TAG_NAME, 'span')


    def viewProfile(self):

        spanList = self.driver.find_elements(*self._SPANS)
        assert len(spanList) >= 1
        viewProfile = None

        for span in spanList:
            if span.text == 'View profile':
                viewProfile = span

        if viewProfile is not None:
            viewProfile.click()
            time.sleep(2)
            return self._returnInstance()
