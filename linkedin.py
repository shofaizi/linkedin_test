from loginPage import LoginPage
from credentials import USER_EMAIL, USER_PASS

def linkedIn_testSuite():
    """
    NOTE:
        This test will run through the Linkedin's platform and test its functionality. It will go through the login, home,
        messaging, profile and jobs pages. This test will also look out for any API responses that will trigger the client
        to alert the user to changes.
    """

    loginPage = LoginPage()

    loginPage.setUp()

    loginPage.setUserEmail(USER_EMAIL)

    homePage = loginPage.setUserPass(USER_PASS)
    homePage.searchUser("Alison Dsa")
    homePage._clickSubmit()



linkedIn_testSuite()