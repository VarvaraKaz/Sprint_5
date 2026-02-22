from pages.main_page import MainPage
from pages.login_page import LoginPage
from conftest import LOGIN_CREDENTIALS


def test_login_via_main_page(driver):
    page = MainPage(driver)
    login_page = LoginPage(driver)

    page.open_main_page()
    page.click_login_button_on_main_page()
    login_page.wait_for_login_page()
    login_page.login(LOGIN_CREDENTIALS["email"], LOGIN_CREDENTIALS["password"])
    login_page.click_login_button()
    assert login_page.is_login_successful()

def test_sauces_tab_is_opened_when_clicked(driver):
    page = MainPage(driver)

    page.open_main_page()
    page.click_sauces_tab()
    assert page.is_sauces_tab_active()

def test_bulki_tab_is_opened_when_clicked(driver):
    page = MainPage(driver)

    page.open_main_page()
    page.click_nachinki_tab()
    page.click_bulki_tab()
    assert page.is_bulki_tab_active()

def test_nachinki_tab_is_opened_when_clicked(driver):
    page = MainPage(driver)

    page.open_main_page()
    page.click_nachinki_tab()
    assert page.is_nachinki_tab_active()

def test_open_personal_account_from_main_page_when_logged_in(login_successful):
    page = MainPage(login_successful.driver)
    assert login_successful.is_login_successful()

    page.click_personal_account()
    assert page.is_personal_account_opened()