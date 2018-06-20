from loginPage import LoginPage
from credentials import USER_EMAIL, USER_PASS
from text import expDescription, volDescription


def profile_test():

    loginPage = LoginPage()

    loginPage.setUp()

    loginPage.setUserEmail(USER_EMAIL)

    homePage = loginPage.setUserPass(USER_PASS)

    profile = homePage.open_ownProfile()
    profile.open_addExperience()
    profile.setExpTitle("Software Developer")
    profile.setExpCompany("Traction On Demand")
    profile.setExpLocation("Vancouver, Canada Area")
    profile.setExpMonth("July")
    profile.setExpYear("2018")
    profile.setExpDescription(expDescription)
    # save
    profile.open_addAccomplishment()
    profile.setVolOrganization("Planet B")
    profile.setVolRole("Software Developer")
    profile.setVolCause("Science and Technology")
    profile.setVolMonth("May")
    profile.setVolYear("2018")
    profile.setVolCurrWork()
    profile.setVolDescription(volDescription)
    # save


profile_test()