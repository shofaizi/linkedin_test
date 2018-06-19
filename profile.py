from base import Base
import time


class Profile(Base):

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


    def getInvitationResult(self):
        """
        Note:
            After sending out an invitation, linkedin will display a "Pending" message to the user.
            This method will get that value so that it can be used to validate in the linkedin.py script
        """

