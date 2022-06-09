import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage


class TestSearchPage:

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.mark.parametrize("data", ["ноутбук", "чайник", "телефон"])
    def test_searching_item_by_valid_name(self, start_page, data):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Enter valid data in Search field and click on search button
            - Verify table with result is present on the screen
        """
        # - Enter valid data in Search field and click on search button
        search_page = start_page.search_item(data)
        #  - Verify table with result is present on the screen
        search_page.verify_table_with_result_is_present()

    @pytest.mark.parametrize("data", ["qwer123", "фівапп", "!@#$%%^"])
    def test_searching_item_by_invalid_name(self, start_page, data):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Enter invalid data in Search field and click on search button
            - Verify result table is absent on the screen
        """
        # - Enter invalid data in Search field and click on search button
        search_page = start_page.search_item(data)
        # - Verify result table is absent on the screen
        search_page.verify_table_with_result_is_absent()
