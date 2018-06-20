from loginPage import LoginPage
from credentials import USER_EMAIL, USER_PASS
from text import description


def profile_test():

    loginPage = LoginPage()

    loginPage.setUp()

    loginPage.setUserEmail(USER_EMAIL)

    homePage = loginPage.setUserPass(USER_PASS)

    profile = homePage.open_ownProfile()
    profile.open_addExperience()
    profile.setTitle("Software Developer")
    profile.setCompany("Traction On Demand")
    profile.setLocation("Vancouver, Canada Area")
    profile.setMonth("July")
    profile.setYear("2018")
    profile.setDescription(description)



profile_test()