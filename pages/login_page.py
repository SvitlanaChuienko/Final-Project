from constants.login_page import LoginPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = LoginPageConstants()

    @log_wrapper
    def login(self, name="", password=""):
        """Login by using available values"""
        self.fill_field(xpath=self.constants.LOGIN_FIELD_XPATH, value=name)
        self.fill_field(xpath=self.constants.PASSWORD_FIELD_XPATH, value=password)
        self.click(xpath=self.constants.LOGIN_BUTTON_XPATH)

    @log_wrapper
    def verify_login_error_message(self):
        """Verifying error message about invalid login"""
        error_message = self.wait_until_displayed(xpath=self.constants.VALIDATION_MESSAGE_XPATH)
        assert error_message.text == self.constants.VALIDATION_MESSAGE_TEXT, "Text isn't valid"

    @log_wrapper
    def navigate_to_sign_up_page(self):
        """Navigate to Sign Up Page by clicking on Sign Up button on Login Page"""
        self.wait_until_clickable(xpath=self.constants.SIGN_UP_BUTTON_XPATH).click()

        from pages.signup_page import SignUpPage
        return SignUpPage(self.driver)
