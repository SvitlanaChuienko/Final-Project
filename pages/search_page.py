from constants.search_page import SearchPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = SearchPageConstants()

    @log_wrapper
    def verify_table_with_result_is_present(self):
        """Verify table with result is present on the screen"""
        result = self.wait_until_displayed(xpath=self.constants.SEARCH_RESULT_TABLE_XPATH)
        assert result.is_displayed()

    @log_wrapper
    def verify_table_with_result_is_absent(self):
        """Verify result table is absent on the screen"""
        assert not self.is_element_exist(xpath=self.constants.SEARCH_RESULT_TABLE_XPATH)

    @log_wrapper
    def navigate_to_item_page_by_item_code(self):
        """Navigate to Item Page by click on item code"""
        self.wait_until_clickable(xpath=self.constants.CODE_ITEM_XPATH).click()

        from pages.item_page import ItemPage
        return ItemPage(self.driver)
