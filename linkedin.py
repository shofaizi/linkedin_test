from base import LoginPage
from selenium import webdriver
from credentials import USER_EMAIL, USER_PASS

def linkedIn_testSuite():

    loginPage = LoginPage()

    loginPage.setUp()

    loginPage.setUserEmail(USER_EMAIL)
    loginPage.setUserPassword(USER_PASS)


linkedIn_testSuite()