from pages.base_page import BasePage
from locators import (MainPageLocators, PersonalAccountLocators, LogInPageLocators)

class PersonalAccountPage(BasePage):

    def open_personal_account(self):
        self.click(MainPageLocators.Personal_Account_Button)

    def click_constructor(self):
        self.click(PersonalAccountLocators.Constructor_Button)

    def is_constuctor_visible(self):
        return self.find_element(MainPageLocators.Constructor_section)

    def click_logo(self):
        self.click(PersonalAccountLocators.Logo)

    def click_logout_button(self):
        self.click(PersonalAccountLocators.Logout_Button)
    
    def is_logout_successful(self):
        return self.find_element(LogInPageLocators.Login_button_Login_Page)
