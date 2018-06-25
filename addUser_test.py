from misc.credentials import USER_EMAIL, USER_PASS
from pages.loginPage import LoginPage
from misc.text import note


def addUserTest():

    loginPage = LoginPage()
    loginPage.setUp()
    loginPage.setUserEmail(USER_EMAIL)
    homePage = loginPage.setUserPass(USER_PASS)

    assert homePage.getPageUrl() == 'https://www.linkedin.com/feed/'
    assert homePage.getTradeMark()

    # search up user and connect
    resultPage = homePage.searchUser("Alison Dsa")
    profilePage = resultPage.openProfile()

    assert profilePage.getPageUrl() == 'https://www.linkedin.com/in/alisondsa/'
    networkPage = profilePage.connectUser(note)

    assert networkPage.getPageUrl() == 'https://www.linkedin.com/mynetwork/invite-sent/alisondsa/?isSendInvite=true'

    # check for invitation status
    profilePage = networkPage.viewProfile()
    assert profilePage.getPageUrl() == 'https://www.linkedin.com/in/alisondsa/'
    assert profilePage.getInvitationStatus() == 'Pending'

addUserTest()