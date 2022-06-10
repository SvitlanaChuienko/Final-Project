from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_wrapper
    def navigate_to_contacts_page_by_number_phone_in_header(self):
        """Navigate to Contacts Page by clicking on phone number in header"""
        self.wait_until_clickable(xpath=self.constants.PHONE_NUMBER_IN_HEADER_XPATH).click()

        from pages.contacts_page import ContactsPage
        return ContactsPage(self.driver)

    @log_wrapper
    def navigate_to_login_page(self):
        """Navigate to Login Page by clicking on Login button in header"""
        self.wait_until_clickable(xpath=self.constants.LOGIN_BUTTON_XPATH).click()

        from pages.login_page import LoginPage
        return LoginPage(self.driver)

    @log_wrapper
    def search_item(self, data):
        """Search item by enter valid data in search field"""
        self.fill_field(xpath=self.constants.SEARCH_FIELD_XPATH, value=data)
        self.click(xpath=self.constants.SEARCH_BUTTON_XPATH)
        from pages.search_page import SearchPage

        return SearchPage(self.driver)

    @log_wrapper
    def verify_new_goods_panel(self):
        """Verify New Goods panel is exist"""
        assert self.wait_until_displayed(xpath=self.constants.NEW_GOODS_PANEL_XPATH)

    @log_wrapper
    def navigate_to_contacts_page_by_contacts_button(self):
        """Navigate to Contacts Page by clicking on Contacts button in navigation panel"""
        self.wait_until_clickable(xpath=self.constants.CONTACTS_BUTTON_XPATH).click()

        from pages.contacts_page import ContactsPage
        return ContactsPage(self.driver)
