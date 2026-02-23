from pages.base_page import BasePage
from locators import (MainPageLocators, PersonalAccountLocators, LogInPageLocators)

class PersonalAccountPage(BasePage):

    def open_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_constructor(self):
        self.click(PersonalAccountLocators.CONSTRUCTOR_BUTTON)

    def is_constuctor_visible(self):
        return self.find_element(MainPageLocators.CONSTRUCTOR_SECTION)

    def click_logo(self):
        self.click(PersonalAccountLocators.LOGO)

    def click_logout_button(self):
        self.click(PersonalAccountLocators.LOGOUT_BUTTON)
    
    def is_logout_successful(self):
        return self.find_element(LogInPageLocators.LOGIN_BUTTON_LOGIN_PAGE)
