import time
from pages.base import Base
from pages.profile import Profile


class Result(Base):

    def openProfile(self):

        time.sleep(1)
        userLink = self.driver.find_element_by_class_name('search-result__result-link')
        userLink.click()
        time.sleep(2)
        # return self._returnInstance()
        return Profile()