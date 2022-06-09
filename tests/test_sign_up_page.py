import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage:

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        user = User()
        user.fill_properties()
        yield user

    def test_success_registration(self, start_page, random_user):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
        Steps:
            - Click Login button
            - Click to Sign Up button
            - Fill field Name, Phone number, Email, Password
            - Click Sign Up button and verify message about success sign up
        """
        # - Click Login button
        login_page = start_page.navigate_to_login_page()
        # - Click to Sign Up button
        signup_page = login_page.navigate_to_sign_up_page()
        # - Fill field Name, Phone number, Email, Password
        signup_page.sign_up(random_user)
        # - Click Sign Up button and verify message about success sign up
        signup_page.click_sign_up_and_verify()
