from pages.base_page import BasePage
from locators import (MainPageLocators, ConstructorLocators, PersonalAccountLocators)
from tests.curl import BASE_URL

class MainPage(BasePage):
    
    def open_main_page(self):
        self.open(BASE_URL)
    
    def click_login_button_on_main_page(self):
        self.click(MainPageLocators.Login_Button_Main_Page)
    
    def click_personal_account(self):
        self.click(MainPageLocators.Personal_Account_Button)

    def is_personal_account_opened(self):
        return self.find_element(PersonalAccountLocators.Logout_Button).is_displayed()

    def click_bulki_tab(self):
        self.click(ConstructorLocators.Bulki_Tab)

    def click_sauces_tab(self):
        self.click(ConstructorLocators.Sauces_Tab)

    def click_nachinki_tab(self):
        self.click(ConstructorLocators.Nachinki_Tab)

    def is_bulki_tab_visible(self):
        return self.find_element(ConstructorLocators.Bulki_Tab).is_displayed()
    
    def is_sauces_tab_visible(self):
        return self.find_element(ConstructorLocators.Sauces_Tab).is_displayed()
    
    def is_nachinki_tab_visible(self):
        return self.find_element(ConstructorLocators.Nachinki_Tab).is_displayed()