from pages.base_page import BasePage
from tests.curl import FORGOR_PASSWORD_URL
from locators import (MainPageLocators, ForgotPasswordPageLocators)


class ForgotPasswordPage(BasePage):

    def open_forgot_password_page(self):
        self.open(FORGOR_PASSWORD_URL)

    def click_login_button(self):
        self.click(ForgotPasswordPageLocators.LOGIN_BUTTON_ON_FORGOT_PASSWORD_PAGE)

    def click_personal_account_button(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)