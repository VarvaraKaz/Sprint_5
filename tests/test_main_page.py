from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_login_via_main_page(driver, LoginCredentials):
    page = MainPage(driver)
    login_page = LoginPage(driver)

    page.open_main_page()
    page.click_login_button_on_main_page()
    login_page.wait_for_login_page()
    login_page.login(LoginCredentials ["email"], LoginCredentials ["password"])
    login_page.click_login_button()
    assert login_page.is_login_successful()

def test_constructor_tabs(driver):
    page = MainPage(driver)

    page.open_main_page()
    page.click_sauces_tab()
    assert page.is_sauces_tab_visible()

    page.click_bulki_tab()
    assert page.is_bulki_tab_visible()

    page.click_nachinki_tab()
    assert page.is_nachinki_tab_visible()

def test_open_personal_account_from_main_page_when_logged_in(login_successful):
    page = MainPage(login_successful.driver)

    page.click_personal_account()
    assert page.is_personal_account_opened()