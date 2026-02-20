from pages.base_page import BasePage
from locators import (LogInPageLocators, MainPageLocators)
from tests.curl import LOGIN_URL

class LoginPage(BasePage):

    def wait_for_login_page(self):
        self.find_element(LogInPageLocators.Email_Login_Input)
    
    def enter_email(self, email):
        self.send_keys(LogInPageLocators.Email_Login_Input, email)

    def enter_password(self, password):
        self.send_keys(LogInPageLocators.Password_Login_Input, password)

    def click_login_button(self):
        self.click(LogInPageLocators.Login_button_Login_Page)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button
    
    def is_login_successful(self):
        return self.find_element(MainPageLocators.Place_Order_Button).is_displayed()
    
    def open_login_page(self):
        self.open(LOGIN_URL)