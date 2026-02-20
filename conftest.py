import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def LoginCredentials():
    return {
        "email": "test123456+1@gmail.com",
        "password": "123456"
    }

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_successful(driver, LoginCredentials):
    page = LoginPage(driver)
    page.open_login_page()
    page.login(
        LoginCredentials["email"],
        LoginCredentials["password"])
    
    page.click_login_button()
    assert page.is_login_successful()

    return page