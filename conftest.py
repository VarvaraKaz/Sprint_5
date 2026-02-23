import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from data import LOGIN_CREDENTIALS

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login_successful(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.login(
        LOGIN_CREDENTIALS["email"],
        LOGIN_CREDENTIALS["password"])
    
    page.click_login_button()
    return page