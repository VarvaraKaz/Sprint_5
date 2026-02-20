from pages.base_page import BasePage
from tests.curl import FORGOR_PASSWORD_URL
from locators import (MainPageLocators, ForgotPasswordPageLocators)


class ForgotPasswordPage(BasePage):

    def open_forgot_password_page(self):
        self.open(FORGOR_PASSWORD_URL)

    def click_login_button(self):
        self.click(ForgotPasswordPageLocators.Login_Button_on_Forgot_Password_Page)

    def click_personal_account_button(self):
        self.click(MainPageLocators.Personal_Account_Button)