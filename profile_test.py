import time

from misc.credentials import USER_EMAIL, USER_PASS
from pages.loginPage import LoginPage


def profile_test():

    loginPage = LoginPage()

    loginPage.setUp()

    loginPage.setUserEmail(USER_EMAIL)

    homePage = loginPage.setUserPass(USER_PASS)

    # assert user details
    homePage.expandProfileNavigator()
    profile = homePage.openOwnProfile()
    time.sleep(3)
    profileDetails = profile.getProfileDetails()

    assert profileDetails['company'] == 'Phantom Screens'
    assert profileDetails['school'] == 'CodeCore Developer Bootcamp'
    assert profileDetails['connections'] == 453
    assert profileDetails['followers'] == 449

    # add experience
    # homePage.expandProfileNavigator()
    # profile = homePage.open_ownProfile()
    # profile.open_addExperience()
    # profile.setExpTitle("Software Developer")
    # profile.setExpCompany("Traction On Demand")
    # profile.setExpLocation("Vancouver, Canada Area")
    # profile.setExpMonth("June")
    # profile.setExpYear("2018")
    # profile.setExpDescription(expDescription)
    # profile.saveExperience()

    # add volunteer work
    # time.sleep(3)
    # profile.open_addVolunteerExperience()
    # profile.setVolOrganization("Planet B")
    # profile.setVolRole("Software Developer")
    # profile.setVolCause("Science and Technology")
    # profile.setVolMonth("May")
    # profile.setVolYear("2018")
    # profile.setVolCurrWork()
    # profile.setVolDescription(volDescription)
    # profile.saveExperience()


    # homePage.logOut()

profile_test()