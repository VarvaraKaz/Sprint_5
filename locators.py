from selenium.webdriver.common.by import By

class RegistrationPageLocators: #Страница Регистрации

    #Поле ввода 'Имя'
    Name_Input = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][1]//input')

    #Поле ввода 'Email'
    Email_Input = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][2]//input')

    #Поле ввода 'Пароль'
    Password_Input = (By.XPATH, '//fieldset[@class="Auth_fieldset__1QzWN mb-6"][3]//input')

    #Кпока 'Зарегистрироваться'
    Register_Button = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//button[text()="Зарегистрироваться"]')

    #Ошибка для некорректного пароля
    Password_Error = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//p[text()="Некорректный пароль"]')

    #Кнопка 'Войти'
    Login_Button_Registration_Page = (By.XPATH, '//a[text()="Войти"]')

 
class MainPageLocators: #Главная Страница

    #Кнопка 'Войти в аккаунт'
    Login_Button_Main_Page = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]//button[text()="Войти в аккаунт"]')

    #Кнопка 'Личный Кабинет' в шапке
    Personal_Account_Button = (By.XPATH, '//p[text()="Личный Кабинет"]')

    #Кнопка 'Оформить Заказ'
    Place_Order_Button = (By.XPATH, '//button[text()="Оформить заказ"]')

    #Блок Конструктор
    Constructor_section = (By.XPATH, '//h1[text()="Соберите бургер"]')

class ConstructorLocators: #Раздел 'Конструктор'

    #Вкладка 'Булки'
    Bulki_Tab = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//span[text()="Булки"]')

    #Вкладка 'Соусы'
    Sauces_Tab = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//span[text()="Соусы"]')

    #Вкладка 'Начинки'
    Nachinki_Tab = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//span[text()="Начинки"]')

class PersonalAccountLocators: #Личный Кабинет

    #Кнопка 'Конструктор' в шапке
    Constructor_Button = (By.XPATH, '//nav[@class="AppHeader_header__nav__g5hnF"]//p[text()="Конструктор"]')

    #Логотип Stellar Burgers
    Logo = (By.XPATH, '//nav[@class="AppHeader_header__nav__g5hnF"]/div[@class="AppHeader_header__logo__2D0X2"]')

    #Кнопка 'Выйти'
    Logout_Button = (By.XPATH, '//ul[@class="Account_list__3KQQf mb-20"]//button[text()="Выход"]')

class LogInPageLocators: #Страница Входа Существующего Пользователя

     #Кнопка 'Восстановить пароль'
     Forgot_Password_Link = (By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//a[text()="Восстановить пароль"]')

     #Поле ввода 'Email'
     Email_Login_Input = (By.XPATH, '//input[@type="text"]')

    #Поле ввода 'Password'
     Password_Login_Input = (By.XPATH, '//input[@type="password"]')

     #Кнопка 'Войти'
     Login_button_Login_Page = (By.XPATH, '//button[text()="Войти"]')

class ForgotPasswordPageLocators: #Страница Восстановления Пароля

    #Кнопка 'Войти'
    Login_Button_on_Forgot_Password_Page = (By.XPATH, '//a[text()="Войти"]')
