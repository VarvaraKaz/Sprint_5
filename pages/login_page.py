from pages.base_page import BasePage
from locators import (LogInPageLocators, MainPageLocators)
from tests.curl import LOGIN_URL

class LoginPage(BasePage):

    def wait_for_login_page(self):
        self.find_element(LogInPageLocators.EMAIL_LOGIN_INPUT)
    
    def enter_email(self, email):
        self.send_keys(LogInPageLocators.EMAIL_LOGIN_INPUT, email)

    def enter_password(self, password):
        self.send_keys(LogInPageLocators.PASSWORD_LOGIN_INPUT, password)

    def click_login_button(self):
        self.click(LogInPageLocators.LOGIN_BUTTON_LOGIN_PAGE)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button
    
    def is_login_successful(self):
        return self.find_element(MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def open_login_page(self):
        self.open(LOGIN_URL)