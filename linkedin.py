from loginPage import LoginPage
from credentials import USER_EMAIL, USER_PASS

def linkedIn_testSuite():
    """
    NOTE:
        This test will run through the Linkedin's platform and test its functionality. It will go through the login, home,
        messaging, profile and jobs pages. This test will look out for API responses when for instance an action triggered
        by the client results in receiving a message.
    """

    loginPage = LoginPage()

    loginPage.setUp()

    loginPage.setUserEmail(USER_EMAIL)
    loginPage.setUserPass(USER_PASS)
    homePage = loginPage.submitLogin()



linkedIn_testSuite()