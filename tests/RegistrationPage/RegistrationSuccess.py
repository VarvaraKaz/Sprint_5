from locators import RegistrationPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random

email = f'testingvar{random.randint(100,999)}@gmail.com'


driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/register")

driver.find_element(*RegistrationPageLocators.Name_Input).send_keys("TestingVarvara")
driver.find_element(*RegistrationPageLocators.Email_Input).send_keys(email)
driver.find_element(*RegistrationPageLocators.Password_Input).send_keys("1q2w3e4r")
driver.find_element(*RegistrationPageLocators.Register_Button).click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

assert driver.current_url == "https://stellarburgers.education-services.ru/"

driver.quit()