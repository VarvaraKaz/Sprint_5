from pages.registration_page import RegistrationPage
import random

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()

    name = 'TestName'
    email = registration_page.generate_email()
    password = '123456'
    registration_page.register_user(name, email, password)
    assert registration_page.is_login_button_displayed()

def test_error_for_password_field(driver):
    page = RegistrationPage(driver)
    page.open_registration_page()

    name = 'TestName'
    email = page.generate_email()
    password = f'{random.randint(1,99999)}'
    page.register_user(name, email, password)
    error_text = page.get_password_error()
    assert 'Некорректный пароль' in error_text