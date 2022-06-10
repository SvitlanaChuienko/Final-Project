from constants.contacts_page import ContactsPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class ContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ContactsPageConstants()

    @log_wrapper
    def verify_contacts_page_is_displayed(self):
        """Verify success redirect to the Contacts Page"""
        contacts_page = self.wait_until_displayed(self.constants.CONTACT_INFO_XPATH)
        assert contacts_page.is_displayed()
