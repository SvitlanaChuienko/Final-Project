from constants.signup_page import SignUpConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class SignUpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = SignUpConstants()

    @log_wrapper
    def sign_up(self, user):
        """Sign up user by using available values"""
        self.fill_field(xpath=self.constants.NAME_FILED_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.USERPHONE_FIELD_XPATH, value=user.phone_number)
        self.fill_field(xpath=self.constants.EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.PASSWORD_FIELD_XPATH, value=user.password)

    def click_sign_up_and_verify(self):
        """Click Sign Up button and verify result"""
        self.wait_until_clickable(xpath=self.constants.SIGN_UP_BUTTON_XPATH).click()
        success_message = self.wait_until_displayed(xpath=self.constants.MESSAGE_SUCCESS_SIGN_UP_XPATH)
        assert success_message.is_displayed()
