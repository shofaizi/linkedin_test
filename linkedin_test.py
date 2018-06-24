from misc.credentials import USER_EMAIL, USER_PASS
from pages.loginPage import LoginPage
from misc.text import note, expDescription, volDescription, post
import time


def linkedIn_testSuite():
    """
    NOTE:
        This test will run through the Linkedin's platform and test its functionality. It will go through the login, home,
        messaging, profile and jobs pages. This test will also look out for any API responses that will trigger the client
        to alert the user to changes.
    """

    # log into Linkedin
    loginPage = LoginPage()
    loginPage.setUp()
    loginPage.setUserEmail(USER_EMAIL)
    homePage = loginPage.setUserPass(USER_PASS)

    assert homePage._getPageUrl() == 'https://www.linkedin.com/feed/?trk='

    # search up user and connect
    resultPage = homePage.searchUser("Alison Dsa")
    profilePage = resultPage.openProfile()

    assert profilePage._getPageUrl() == 'https://www.linkedin.com/in/alisondsa/'
    networkPage = profilePage.connectUser(note)

    assert networkPage._getPageUrl() == 'https://www.linkedin.com/mynetwork/invite-sent/alisondsa/?isSendInvite=true'

    # check for invitation status
    profilePage = networkPage.viewProfile()
    assert profilePage._getPageUrl() == 'https://www.linkedin.com/in/alisondsa/'
    assert profilePage.getInvitationStatus() == 'Pending'

    # go to profile and add work/volunteer experience
    profilePage.expandProfileNavigator()
    profile = homePage.open_ownProfile()
    assert profile._getPageUrl() == 'https://www.linkedin.com/in/shoaibfaizi/'
    profile.open_addExperience()
    profile.setExpTitle("Front End Software Developer")
    profile.setExpCompany("Phantom Screens")
    profile.setExpLocation("Abbotsford, Canada Area")
    profile.setExpMonth("September")
    profile.setExpYear("2017")
    profile.setExpDescription(expDescription)
    profile.saveExperience()

    # add volunteer work
    time.sleep(3)
    profile.open_addVolunteerExperience()
    profile.setVolOrganization("Planet B")
    profile.setVolRole("Software Developer")
    profile.setVolCause("Science and Technology")
    profile.setVolMonth("May")
    profile.setVolYear("2018")
    profile.setVolCurrWork()
    profile.setVolDescription(volDescription)
    profile.saveExperience()

    # check user details
    profileDetails = profile.getProfileDetails()

    assert profileDetails['company'] == 'Phantom Screens'
    assert profileDetails['school'] == 'CodeCore Developer Bootcamp'
    assert profileDetails['connections'] == 453
    assert profileDetails['followers'] == 449

    # navigate to home page and share a post
    assert homePage._getPageUrl() == 'https://www.linkedin.com/feed/?trk='
    homePage.sharePost(post)

    # log out and close driver
    homePage.logOut()
    homePage.tearDown()

linkedIn_testSuite()
