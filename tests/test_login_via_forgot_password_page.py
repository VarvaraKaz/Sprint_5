from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage

class TestLoginViaForgotPage:
    def test_login_via_forgot_password_page(self, driver): 
        forgot_page = ForgotPasswordPage(driver) 
        login_page = LoginPage(driver) 
    
        forgot_page.open_forgot_password_page() 
        forgot_page.click_login_button() 
        login_page.login_as_valid_user()
        assert login_page.is_login_successful()

    def test_login_via_personal_account_button_on_forgot_password_page(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        login_page = LoginPage(driver)

        forgot_page.open_forgot_password_page()
        forgot_page.click_personal_account_button()
        login_page.login_as_valid_user()
        assert login_page.is_login_successful()