from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from home import Home
from base import Base


class LoginPage(Base):

    EMAIL_INPUT = (By.ID, "login-email")
    PASSWORD_INPUT = (By.ID, "login-password")
    LOGIN_SUBMIT = (By.ID, "login-submit")



    def setUserEmail(self, value):

        email = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self.EMAIL_INPUT))
        )

        self._sendKeys(email, value)


    def setUserPass(self, value):

        password = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self.PASSWORD_INPUT))
        )

        self._sendKeys(password, value)


    def submitLogin(self):

        self._clickSubmit(self.LOGIN_SUBMIT)

        return Home()
