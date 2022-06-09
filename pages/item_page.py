from constants.item_page import ItemPageConstant
from pages.base_page import BasePage
from pages.utils import log_wrapper


class ItemPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ItemPageConstant()

    @log_wrapper
    def add_item_to_basket_and_verify_popup(self):
        """Add item to basket and verify success popup"""
        self.wait_until_clickable(xpath=self.constants.ADD_TO_BASKET_BUTTON_XPATH).click()
        success_popup = self.wait_until_displayed(xpath=self.constants.ADDED_ITEM_POPUP_XPATH)
        assert success_popup.is_displayed()
        self.click(xpath=self.constants.CLOSE_ADDED_ITEM_POPUP_XPATH)

    @log_wrapper
    def navigate_to_basket_page(self):
        """Navigate from Item Page to Basket Page"""
        self.wait_until_clickable(xpath=self.constants.BASKET_BUTTON_XPATH).click()
        from pages.basket_page import BasketPage
        return BasketPage(self.driver)
