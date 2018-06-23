import time
from pages.base import Base


class Network(Base):


    def viewProfile(self):

        viewButton = self.driver.find_elements_by_class_name('mn-heathrow-toast__action-btn')
        viewButton.click()
        time.sleep(2)
        return self._returnInstance()
