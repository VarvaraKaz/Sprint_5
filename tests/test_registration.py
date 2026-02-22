from pages.registration_page import RegistrationPage
import random
from generators import Generate_Email
from data import TEST_NAME, TEST_PASSWORD

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()

    name = TEST_NAME
    email = Generate_Email()
    password = TEST_PASSWORD
    registration_page.register_user(name, email, password)
    assert registration_page.is_login_button_displayed()

def test_error_for_password_field(driver):
    page = RegistrationPage(driver)
    page.open_registration_page()

    name = TEST_NAME
    email = Generate_Email()
    password = f'{random.randint(1,99999)}'
    page.register_user(name, email, password)
    error_text = page.get_password_error()
    assert 'Некорректный пароль' in error_text