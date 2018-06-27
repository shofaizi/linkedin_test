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

        Implemented test types: Functional, Static, Links tests
    """


    # log into Linkedin
    loginPage = LoginPage()
    loginPage.setUp()
    loginPage.setUserEmail(USER_EMAIL)
    homePage = loginPage.setUserPass(USER_PASS)

    assert homePage.getPageUrl() == 'https://www.linkedin.com/feed/'

    # search up user and connect
    resultPage = homePage.searchUser("Alison Dsa")
    assert resultPage.getPageUrl() == 'https://www.linkedin.com/search/results/index/?keywords=Alison%20Dsa&origin=GLOBAL_SEARCH_HEADER'

    profilePage = resultPage.openProfile()
    assert profilePage.getPageUrl() == 'https://www.linkedin.com/in/alisondsa/'

    networkPage = profilePage.connectUser(note)

    assert networkPage.getPageUrl() == 'https://www.linkedin.com/mynetwork/invite-sent/alisondsa/?isSendInvite=true'

    # check for invitation status
    profilePage = networkPage.viewProfile()
    assert profilePage.getPageUrl() == 'https://www.linkedin.com/in/alisondsa/'
    assert profilePage.getInvitationStatus() == 'Pending'

    # go to profile and add work/volunteer experience
    profilePage.expandProfileNavigator()
    profilePage.openOwnProfile()
    assert profilePage.getPageUrl() == 'https://www.linkedin.com/in/shoaibfaizi/'
    profilePage.openAddExperience()
    profilePage.setExpTitle("Front End Software Developer")
    profilePage.setExpCompany("Phantom Screens")
    profilePage.setExpLocation("Abbotsford, Canada Area")
    profilePage.setExpMonth("September")
    profilePage.setExpYear("2017")
    profilePage.setExpDescription(expDescription)
    profilePage.saveExperience()

    # add volunteer work
    time.sleep(2)
    profilePage.openAddVolunteerExperience()
    profilePage.setVolOrganization("Planet B")
    profilePage.setVolRole("Software Developer")
    profilePage.setVolCause("Science and Technology")
    profilePage.setVolMonth("May")
    profilePage.setVolYear("2018")
    profilePage.setVolCurrWork()
    profilePage.setVolDescription(volDescription)
    profilePage.saveExperience()

    # check user details
    profileDetails = profilePage.getProfileDetails()

    assert profileDetails['company'] == 'Phantom Screens'
    assert profileDetails['school'] == 'CodeCore Developer Bootcamp'
    assert profileDetails['connections'] == 453
    # assert profileDetails['followers'] == 449

    # navigate to home page and share a post
    homePage = profilePage.goToHomePage()
    assert homePage.getPageUrl() == 'https://www.linkedin.com/feed/'
    homePage.sharePost(post)
    assert homePage.getTradeMark()

    # log out and close driver
    homePage.logOut()
    homePage.tearDown()



linkedIn_testSuite()
