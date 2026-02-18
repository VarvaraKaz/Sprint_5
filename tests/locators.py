from selenium import webdriver
from selenium.webdriver.common.by import By

class RegistrationPageLocators: #Страница Регистрации

    #Поле ввода 'Имя'
    Name_Input = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//label[text()="Имя"]')

    #Поле ввода 'Email'
    Email_Input = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//label[text()="Email"]')

    #Поле ввода 'Пароль'
    Password_Input = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//label[text()="Пароль"]')

    #Кпока 'Зарегистрироваться'
    Register_Button = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//button[text()="Зарегистрироваться"]')

    #Ошибка для некорректного пароля
    Password_Error = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//p[text()="Некорректный пароль"]')
 
class MainPageLocators: #Главная Страница

    #Кнопка 'Войти в аккаунт'
    Login_Button = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]//button[text()="Войти в аккаунт"]')

    #Кнопка 'Личный Кабинет' в шапке
    Personal_Account_Button = (By.XPATH, '//nav[@class="AppHeader_header__nav__g5hnF"]//p[text()="Личный Кабинет"]')

class Constructor: #Раздел 'Конструктор'

    #Вкладка 'Булки'
    Bulki_Tab = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//span[text()="Булки"]')

    #Вкладка 'Соусы'
    Sauces_Tab = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//span[text()="Соусы"]')

    #Вкладка 'Начинки'
    Nachinki_Tab = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//span[text()="Начинки"]')

class PesronalAccount: #Личный Кабинет

    #Кнопка 'Конструктор' в шапке
    Constructor_Button = (By.XPATH, '//nav[@class="AppHeader_header__nav__g5hnF"]//p[text()="Конструктор"]')

    #Логотип Stellar Burgers
    Logo = (By.XPATH, '//nav[@class="AppHeader_header__nav__g5hnF"]/div[@class="AppHeader_header__logo__2D0X2"]')

    #Кнопка 'Выйти'
    Logout_Button = (By.XPATH, '//ul[@class="Account_list__3KQQf mb-20"]//button[text()="Выход"]')

class LogInPage: #Страница Входа Существующего Пользователя

     #Кнопка 'Восстановить пароль'
     Forgot_Password_Link = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//a[text()="Восстановить пароль"]')

class ForgorPasswordPage: #Страница Восстановления Пароля

    #Кнопка 'Восстановить'
    Forgot_Password_Button = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//button[text()="Восстановить"]')
