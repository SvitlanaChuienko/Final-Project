from constants.basket_page import BasketPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class BasketPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = BasketPageConstants()

    @log_wrapper
    def verify_added_item_in_basket(self):
        """Verifying item is added in basket by absent message about empty basket"""
        assert not self.is_element_exist(xpath=self.constants.EMPTY_BASKET_MESSAGE_XPATH)

    @log_wrapper
    def delete_item_and_verify_empty_basket(self):
        """Click 'Delete' button and verify message about empty basket"""
        self.wait_until_clickable(xpath=self.constants.DELETE_ITEM_BUTTON_XPATH).click()
        message_empty_basket = self.wait_until_displayed(xpath=self.constants.EMPTY_BASKET_MESSAGE_XPATH)
        assert message_empty_basket.text == self.constants.EMPTY_BASKET_MESSAGE_TEXT, "Text isn't valid"
