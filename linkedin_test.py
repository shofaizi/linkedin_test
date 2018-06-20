from loginPage import LoginPage
from credentials import USER_EMAIL, USER_PASS

note = "Hello, my name is Shoaib Faizi and I am developing an automated test suite " \
       "to make sure Linkedin's features work right. Have a good day."

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

    resultPage = homePage.searchUser("Alison Dsa")
    profilePage = resultPage.openProfile()
    profilePage.connectUser(note)


linkedIn_testSuite()