from pages.base_page import BasePage
from locators import (MainPageLocators, ConstructorLocators, PersonalAccountLocators)
from tests.curl import BASE_URL

class MainPage(BasePage):
    
    def open_main_page(self):
        self.open(BASE_URL)
    
    def click_login_button_on_main_page(self):
        self.click(MainPageLocators.LOGIN_BUTTON_MAIN_PAGE)
    
    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def is_personal_account_opened(self):
        return self.find_element(PersonalAccountLocators.LOGOUT_BUTTON).is_displayed()

    def click_bulki_tab(self):
        self.click(ConstructorLocators.BULKI_TAB)

    def click_sauces_tab(self):
        self.click(ConstructorLocators.SAUCES_TAB)

    def click_nachinki_tab(self):
        self.click(ConstructorLocators.NACHINKI_TAB)

    def is_tab_active(self, tab_locator):
        element = self.find_element(tab_locator)
        return "tab_tab_type_current" in element.get_attribute("class")

    def is_bulki_tab_active(self):
        return self.is_tab_active(ConstructorLocators.BULKI_TAB)
    
    def is_sauces_tab_active(self):
        return self.is_tab_active(ConstructorLocators.SAUCES_TAB)
    
    def is_nachinki_tab_active(self):
        return self.is_tab_active(ConstructorLocators.NACHINKI_TAB)