from pages.base_page import BasePage
from locators import (RegistrationPageLocators, LogInPageLocators, MainPageLocators)
from tests.curl import REGISTRATION_URL

class RegistrationPage(BasePage):

    def open_registration_page(self):
        self.open(REGISTRATION_URL)

    def enter_name(self, name):
        self.send_keys(RegistrationPageLocators.NAME_INPUT, name)

    def enter_email(self, email):
        self.send_keys(RegistrationPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(RegistrationPageLocators.PASSWORD_INPUT, password)

    def click_register(self):
        self.click(RegistrationPageLocators.REGISTER_BUTTON)

    def get_password_error(self):
        return self.get_text(RegistrationPageLocators.PASSWORD_ERROR)
    
    def register_user(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register()

    def is_login_button_displayed(self):
        return self.find_element(LogInPageLocators.LOGIN_BUTTON_LOGIN_PAGE).is_displayed()
    
    def click_login_button(self):
        self.click(RegistrationPageLocators.LOGIN_BUTTON_REGISTRATION_PAGE)

    def click_personal_account_button(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)