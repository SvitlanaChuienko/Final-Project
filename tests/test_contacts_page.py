import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage


class TestContactsPage:

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    def test_redirect_to_contacts_page_by_clicking_on_phone_number(self, start_page):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Find 'Phone number' in header and click on it
            - Verify redirect on the contacts page
        """
        # - Find 'Phone number' in header and click on it
        contacts_page = start_page.navigate_to_contacts_page_by_number_phone_in_header()
        # - Verify redirect on the contacts page
        contacts_page.verify_contacts_page_is_displayed()

    def test_redirect_to_contacts_page_by_clicking_on_contacts_button(self, start_page):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Find 'Contacts' button in navigation panel and click on it
            - Verify redirect on the contacts page
        """
        # - Find 'Contacts' button in navigation panel and click on it
        contacts_page = start_page.navigate_to_contacts_page_by_contacts_button()
        # - Verify redirect on the contacts page
        contacts_page.verify_contacts_page_is_displayed()
