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
    _ANCHOR_TAGS = (By.TAG_NAME, 'a')
    _ME_LINK = (By.ID, 'nav-settings__dropdown-trigger')
    _VIEW_PROFILE_BUTTON = (By.CLASS_NAME, 'button-tertiary-medium')

    _EXPERIENCE_TITLE = (By.ID, 'position-title-typeahead')
    _EXPERIENCE_COMPANY = (By.ID, 'position-company-typeahead')
    _EXPERIENCE_LOCATION = (By.ID, 'position-location-typeahead')
    _EXPERIENCE_MONTH = (By.ID, 'position-start-month')
    _EXPERIENCE_YEAR = (By.ID, 'position-start-year')
    _EXPERIENCE_DESCRIPTION = (By.ID, 'position-description')
    _EXPERIENCE_SAVE_BUTTON = (By.CLASS_NAME, 'form-submit-action')

    _VOLUNTEER_ORGANIZATION = (By.NAME, "companyName")
    _VOLUNTEER_ROLE = (By.NAME, "role")
    _VOLUNTEER_CAUSE = (By.ID, "volunteer-experience-cause")
    _VOLUNTEER_START_MONTH = (By.ID, "volunteer-experience-start-month")
    _VOLUNTEER_START_YEAR = (By.ID, "volunteer-experience-start-year")
    _VOLUNTEER_CURRENTLY_WORKING = (By.ID, "volunteer-experience-currently-volunteers-here")
    _VOLUNTEER_DESCRIPTION = (By.NAME, "description")



    myProfileUrl = 'https://www.linkedin.com/in/shoaibfaizi/'

    def getCheckbox(self):

        inputList = self.driver.find_elements_by_tag_name('label')
        checkbox = None

        for input in inputList:
            if input.get_attribute('for') == 'volunteer-experience-currently-volunteers-here':
                checkbox = input

        return checkbox


    def saveExperience(self):

        buttons = self.driver.find_elements_by_tag_name('button')
        save = None

        for button in buttons:
            if button.get_attribute('class') == 'pe-form-footer__action--submit form-submit-action Sans-15px-white-100%':
                save = button

        self._clickSubmit(save)


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

        self.driver.get('https://www.linkedin.com/in/shoaibfaizi/edit/position/new/')


    def open_addVolunteerExperience(self):

        self.driver.get('https://www.linkedin.com/in/shoaibfaizi/edit/volunteer-experience/new/')


    def setExpTitle(self, value):

        titleField = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_TITLE))
        )

        self._sendKeys(titleField, value)


    def setExpCompany(self, value):

        companyField = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_COMPANY))
        )

        self._sendKeys(companyField, value)
        time.sleep(1)


    def setExpLocation(self, value):

        locationField = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_LOCATION))
        )

        self._sendKeys(locationField, value)
        time.sleep(1)


    def setExpMonth(self, value):

        monthSelect = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_MONTH))
        )

        Select(monthSelect).select_by_visible_text(value)
        time.sleep(1)


    def setExpYear(self, value):

        yearSelect = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_YEAR))
        )

        Select(yearSelect).select_by_visible_text(value)
        time.sleep(1)


    def setExpDescription(self, value):

        descriptionField =  WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._EXPERIENCE_DESCRIPTION))
        )

        self._sendKeys(descriptionField, value)
        time.sleep(1)


    def setVolOrganization(self, value):

        organizationField =  WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._VOLUNTEER_ORGANIZATION))
        )

        self._sendKeys(organizationField, value)
        time.sleep(1)


    def setVolRole(self, value):

        roleField =  WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._VOLUNTEER_ROLE))
        )

        self._sendKeys(roleField, value)
        time.sleep(1)


    def setVolCause(self, value):

        cause = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._VOLUNTEER_CAUSE))
        )

        Select(cause).select_by_visible_text(value)
        time.sleep(1)


    def setVolMonth(self, value):

        month = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._VOLUNTEER_START_MONTH))
        )

        Select(month).select_by_visible_text(value)
        time.sleep(1)


    def setVolYear(self, value):

        year = WebDriverWait(self.driver, self.longWait).until(
            EC.visibility_of_element_located((self._VOLUNTEER_START_YEAR))
        )

        Select(year).select_by_visible_text(value)
        time.sleep(1)


    def setVolCurrWork(self):

        checkbox = self.getCheckbox()

        checkbox.click()


    def setVolDescription(self, value):

        descriptionFields =  self.driver.find_elements_by_tag_name('textarea')
        description = None

        if len(descriptionFields) == 1:
            self._sendKeys(descriptionFields[0], value)
        # self._sendKeys(descriptionField, value)
        time.sleep(1)


    # def saveExperienceForm(self):
    #     data-is-animating-click