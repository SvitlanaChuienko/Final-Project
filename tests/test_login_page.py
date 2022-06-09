import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage


class TestLoginPage:

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    def test_login_with_empty_fields(self, start_page):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
        Steps:
            - Click Login button
            - Click and clear login field
            - Click and clear password field
            - Click on 'Login' button
            - Verify error message
        """
        # - Click Login button
        login_page = start_page.navigate_to_login_page()
        # - Click and clear login field
        # - Click and clear password field
        # - Click on 'Login' button
        login_page.login()
        # - Verify error message
        login_page.verify_login_error_message()
