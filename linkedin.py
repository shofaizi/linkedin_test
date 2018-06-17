from base import LoginPage
from selenium import webdriver
from credentials import USER_EMAIL

def linkedIn_testSuite():

    loginPage = LoginPage()

    loginPage.setUp()

    loginPage.setUserEmail(USER_EMAIL)


linkedIn_testSuite()