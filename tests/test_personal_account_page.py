from pages.personal_account_page import PersonalAccountPage

def test_open_constructor_from_personal_account_page(login_successful):
    main_page = login_successful
    assert login_successful.is_login_successful()
    personal_account_page = PersonalAccountPage(main_page.driver)
    
    personal_account_page.open_personal_account()
    personal_account_page.click_constructor()
    assert personal_account_page.is_constuctor_visible()

def test_click_logo_from_personal_account_page(login_successful):
    main_page = login_successful
    assert login_successful.is_login_successful()

    personal_account_page = PersonalAccountPage(main_page.driver)

    personal_account_page.open_personal_account()
    personal_account_page.click_logo()
    assert personal_account_page.is_constuctor_visible()

def test_logout_from_personal_account_page(login_successful):
    main_page = login_successful
    assert login_successful.is_login_successful()

    personal_account_page = PersonalAccountPage(main_page.driver)

    personal_account_page.open_personal_account()
    personal_account_page.click_logout_button()
    assert personal_account_page.is_logout_successful()

