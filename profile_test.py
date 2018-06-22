from loginPage import LoginPage
from credentials import USER_EMAIL, USER_PASS
from text import expDescription, volDescription
import time


def profile_test():

    loginPage = LoginPage()

    loginPage.setUp()

    loginPage.setUserEmail(USER_EMAIL)

    homePage = loginPage.setUserPass(USER_PASS)

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