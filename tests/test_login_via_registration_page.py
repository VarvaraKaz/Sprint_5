from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage

def test_login_via_registration_page(driver, LoginCredentials):
    registration_page = RegistrationPage(driver)
    login_page = LoginPage(driver)

    registration_page.open_registration_page()
    registration_page.click_login_button()
    login_page.wait_for_login_page()
    login_page.login(LoginCredentials ["email"], LoginCredentials ["password"])
    login_page.click_login_button()
    assert login_page.is_login_successful()

def test_login_via_personal_account_button_on_registration_page(driver, LoginCredentials):
    registration_page = RegistrationPage(driver)
    login_page = LoginPage(driver)

    registration_page.open_registration_page()
    registration_page.click_personal_account_button()
    login_page.wait_for_login_page()
    login_page.login(LoginCredentials ["email"], LoginCredentials ["password"])
    login_page.click_login_button()
    assert login_page.is_login_successful()