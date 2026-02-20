from pages.base_page import BasePage
from locators import (RegistrationPageLocators, LogInPageLocators, MainPageLocators)
from tests.curl import REGISTRATION_URL
import random

class RegistrationPage(BasePage):

    def open_registration_page(self):
        self.open(REGISTRATION_URL)

    def enter_name(self, name):
        self.send_keys(RegistrationPageLocators.Name_Input, name)

    def enter_email(self, email):
        self.send_keys(RegistrationPageLocators.Email_Input, email)

    def enter_password(self, password):
        self.send_keys(RegistrationPageLocators.Password_Input, password)

    def click_register(self):
        self.click(RegistrationPageLocators.Register_Button)

    def get_password_error(self):
        return self.get_text(RegistrationPageLocators.Password_Error)
    
    def register_user(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register()

    def is_login_button_displayed(self):
        return self.find_element(LogInPageLocators.Login_button_Login_Page).is_displayed()
    
    def click_login_button(self):
        self.click(RegistrationPageLocators.Login_Button_Registration_Page)

    def click_personal_account_button(self):
        self.click(MainPageLocators.Personal_Account_Button)

    @staticmethod
    def generate_email():
        return f'varvara_kazarosian_40_{random.randint(100,999)}@gmail.com'