from selenium.webdriver.common.by import By

class RegistrationPageLocators: #Страница Регистрации

    #Поле ввода 'Имя'
    NAME_INPUT = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][1]//input')

    #Поле ввода 'Email'
    EMAIL_INPUT = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][2]//input')

    #Поле ввода 'Пароль'
    PASSWORD_INPUT = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][3]//input')

    #Кпока 'Зарегистрироваться'
    REGISTER_BUTTON = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//button[text()="Зарегистрироваться"]')

    #Ошибка для некорректного пароля
    PASSWORD_ERROR = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//p[text()="Некорректный пароль"]')

    #Кнопка 'Войти'
    LOGIN_BUTTON_REGISTRATION_PAGE = (By.XPATH, '//a[text()="Войти"]')

 
class MainPageLocators: #Главная Страница

    #Кнопка 'Войти в аккаунт'
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]//button[text()="Войти в аккаунт"]')

    #Кнопка 'Личный Кабинет' в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')

    #Кнопка 'Оформить Заказ'
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    #Блок Конструктор
    CONSTRUCTOR_SECTION = (By.XPATH, '//h1[text()="Соберите бургер"]')

class ConstructorLocators: #Раздел 'Конструктор'

    #Вкладка 'Булки'
    BULKI_TAB = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//div[span[text()="Булки"]]')

    #Вкладка 'Соусы'
    SAUCES_TAB = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//div[span[text()="Соусы"]]')

    #Вкладка 'Начинки'
    NACHINKI_TAB = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//div[span[text()="Начинки"]]')

class PersonalAccountLocators: #Личный Кабинет

    #Кнопка 'Конструктор' в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, '//nav[@class="AppHeader_header__nav__g5hnF"]//p[text()="Конструктор"]')

    #Логотип Stellar Burgers
    LOGO = (By.XPATH, '//nav[@class="AppHeader_header__nav__g5hnF"]/div[@class="AppHeader_header__logo__2D0X2"]')

    #Кнопка 'Выйти'
    LOGOUT_BUTTON = (By.XPATH, '//ul[@class="Account_list__3KQQf mb-20"]//button[text()="Выход"]')

class LogInPageLocators: #Страница Входа Существующего Пользователя

     #Кнопка 'Восстановить пароль'
     FORGOT_PASSWORD_LINK = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//a[text()="Восстановить пароль"]')

     #Поле ввода 'Email'
     EMAIL_LOGIN_INPUT = (By.XPATH, '//input[@type="text"]')

    #Поле ввода 'Password'
     PASSWORD_LOGIN_INPUT = (By.XPATH, '//input[@type="password"]')

     #Кнопка 'Войти'
     LOGIN_BUTTON_LOGIN_PAGE = (By.XPATH, '//button[text()="Войти"]')

class ForgotPasswordPageLocators: #Страница Восстановления Пароля

    #Кнопка 'Войти'
    LOGIN_BUTTON_ON_FORGOT_PASSWORD_PAGE = (By.XPATH, '//a[text()="Войти"]')
