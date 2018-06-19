from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from base import Base


class LoginPage(Base):

    _EMAIL_INPUT = (By.ID, "login-email")
    _PASSWORD_INPUT = (By.ID, "login-password")
    _LOGIN_SUBMIT = (By.ID, "login-submit")


    def setUserEmail(self, value):

        email = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EMAIL_INPUT))
        )

        self._sendKeys(email, value)


    def setUserPass(self, value):

        password = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._PASSWORD_INPUT))
        )

        self._sendKeys(password, value)
        return self._returnInstance()


    def submitLogin(self):

        self._clickSubmit((self._LOGIN_SUBMIT))
        return self._returnInstance()
