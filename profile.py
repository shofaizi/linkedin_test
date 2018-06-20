from base import Base
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Profile(Base):

    _SPANS = (By.TAG_NAME, 'span')
    _H1 = (By.TAG_NAME, 'h1')
    _BUTTONS = (By.TAG_NAME, 'button')
    _EXPAND_BIO_BUTTON = (By.CLASS_NAME, 'pv-profile-section__card-action-bar')
    # _ADD_POSITION_BUTTON = (By.CLASS_NAME, 'pv-profile-section__header-add-action')
    _ANCHOR_TAGS = (By.TAG_NAME, 'a')
    _ME_LINK = (By.ID, 'nav-settings__dropdown-trigger')
    _VIEW_PROFILE_BUTTON = (By.CLASS_NAME, 'button-tertiary-medium')

    _EXPERIENCE_TITLE = (By.ID, 'position-title-typeahead')
    _EXPERIENCE_COMPANY = (By.ID, 'position-company-typeahead')
    _EXPERIENCE_LOCATION = (By.ID, 'position-location-typeahead')
    _EXPERIENCE_MONTH = (By.ID, 'position-start-month')
    _EXPERIENCE_YEAR = (By.ID, 'position-start-year')
    _EXPERIENCE_DESCRIPTION = (By.ID, 'position-description')


    myProfileUrl = 'https://www.linkedin.com/in/shoaibfaizi/'


    def connectUser(self, value):

        time.sleep(2)

        # click on connect button
        button = self.driver.find_element_by_class_name('button-primary-large')
        button.click()

        time.sleep(2)
        note = self.driver.find_element_by_class_name('send-invite__actions')
        noteWrapper = note.find_elements_by_tag_name("button")
        noteWrapper[0].click()

        # compose message
        message = self.driver.find_element_by_name('message')
        message.send_keys(value)

        # send invitation
        # sendButton = self.driver.find_element_by_class_name('button-primary-large')
        # sendButton.click()
        noteWrapper[1].click()
        time.sleep(2)
        self._returnInstance()


    def getInvitationResult(self):
        """
        Note:
            After sending out an invitation, linkedin will display a "Pending" message to the user.
            This method will get that value so that it can be used to validate in the linkedin_test.py script
        """

        div = self.driver.find_element_by_class_name('pv-top-card-v2-section__actions')
        button = div.find_elements_by_tag_name('button')[0]
        span = button.find_elements_by_class_name('pv-s-profile-actions__label')
        return span.text


    def getProfileDetails(self):
        """
        Note:
            Gets all spans for a class and filters out the ones that match a given class name

        Return:
            String presenting the current work experience
        """

        spans = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_all_elements_located((self._SPANS))
        )

        details = list(filter(lambda span: span.get_attribute('class') == 'pv-top-card-v2-sction__entity-name', spans))
        print(details)
        assert len(details) == 4

        detailsDict = {}

        for detail in details:
            detailsDict[detail.text] = detail.text

        print(detailsDict)


    def getFullName(self):

        h1 = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_all_elements_located((self._H1))
        )

        fullName = list(filter(lambda x: x.get_attribute('class') == 'pv-top-card-section__name', h1))
        print(fullName)
        assert len(fullName) == 1

        return fullName[0]


    def expandBioSection(self):


        expandButton = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPAND_BIO_BUTTON))
        )

        expandButton.click()


    def open_addExperience(self):

        # addButton = WebDriverWait(self.driver, self.longWait).until(
        #     EC.visibility_of_element_located((self._ADD_POSITION_BUTTON))
        # )

        time.sleep(3)
        profileDetailsDiv = self.driver.find_element_by_class_name('profile-detail')
        profileDetailsDiv.find
        anchorTags = self.driver.find_elements_by_tag_name('a')

        print(anchorTags)

        addButton = list(filter(lambda x: print(x.get_attribute('data-control-name')), anchorTags))

        print('add buttons: ', addButton)
        addButton[0].click()


    def open_addAccomplishment(self, value):

        buttons = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_all_elements_located((self._BUTTONS))
        )

        expandList = list(filter(lambda x: x.get_attribute('data-control-name') == 'add_accomplishment', buttons))
        assert len(expandList) == 1

        expandList[0].click()

        anchorTags = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_all_elements_located((self._ANCHOR_TAGS))
        )

        value = "add_" + str(value.lower())

        links = list(filter(lambda x: x.get_attribute('data-control-name') == 'add_accomplishment'))


    def setTitle(self, value):

        titleField = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_TITLE))
        )

        self._sendKeys(titleField, value)


    def setCompany(self, value):

        companyField = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_COMPANY))
        )

        self._sendKeys(companyField, value)
        time.sleep(1)


    def setLocation(self, value):

        locationField = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_LOCATION))
        )

        self._sendKeys(locationField, value)
        time.sleep(1)


    def setMonth(self, value):

        monthSelect = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_MONTH))
        )

        Select(monthSelect).select_by_visible_text(value)
        time.sleep(1)


    def setYear(self, value):

        yearSelect = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_YEAR))
        )

        Select(yearSelect).select_by_visible_text(value)
        time.sleep(1)


    def setDescription(self, value):

        descriptionField =  WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_DESCRIPTION))
        )

        self._sendKeys(descriptionField, value)
        time.sleep(1)


    # def saveExperienceForm(self):
    #     data-is-animating-click