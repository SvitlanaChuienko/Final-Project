import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage


class TestBasketPage:

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def add_item_to_basket(self, start_page):
        search_page = start_page.search_item(data="795911")
        item_page = search_page.navigate_to_item_page_by_item_code()
        item_page.add_item_to_basket_and_verify_popup()

        yield item_page

    def test_add_item_in_basket_by_searching_item_code(self, start_page):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Find "Search form" and click on it
            - Enter valid data
            - Click on search button
            - Open Item Page by click on the item code
            - Click "Add to basket" button and verify success added popup
            - Click Basket button
            - Verify items in basket = 1
        """
        # - Find "Search form" and click on it
        # - Enter valid data
        # - Click on search button
        search_page = start_page.search_item(data='795911')
        # - Open Item Page by click on the item code
        item_page = search_page.navigate_to_item_page_by_item_code()
        # - Click "Add to basket" button and verify success added popup
        item_page.add_item_to_basket_and_verify_popup()
        #  Click Basket button
        basket_page = item_page.navigate_to_basket_page()
        # - Verify items in basket = 1
        basket_page.verify_added_item_in_basket()

    def test_delete_item_from_basket(self, start_page, add_item_to_basket):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
            - Add item in basket
        - Steps:
            - Click on basket button
            - Click on "Delete" button on Basket Page
            - Verify message about empty basket
        """
        # - Click on basket button
        basket_page = add_item_to_basket.navigate_to_basket_page()
        # - Click on "Delete" button on Item page
        # - Verify message about empty basket
        basket_page.delete_item_and_verify_empty_basket()

    def test_back_button_on_basket_page(self, start_page, add_item_to_basket):
        """
        -Pre-conditions:
            - Create driver
            - Open start page
            - Add item in basket
        - Steps:
            - Click on basket button
            - Click "Back" button
            - Verify Start Page by find New Goods Panel
        """
        # - Click on basket button
        basket_page = add_item_to_basket.navigate_to_basket_page()
        # - Click "Back" button
        start_page = basket_page.navigate_to_start_page()
        # - Verify Start Page by find New Goods Panel
        start_page.verify_new_goods_panel()
