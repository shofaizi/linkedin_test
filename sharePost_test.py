from misc.credentials import USER_EMAIL, USER_PASS
from misc.text import post
from pages.loginPage import LoginPage


def sharePost():

    loginPage = LoginPage()
    loginPage.setUp()
    loginPage.setUserEmail(USER_EMAIL)
    homePage = loginPage.setUserPass(USER_PASS)
    homePage.sharePost(post)

sharePost()
