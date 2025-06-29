from pages.locators import create_customer_account_locators_page as loc

def test_create_customer_account_when_email_already_used(create_customer_account_page):
    create_customer_account_page.open_page()
    create_customer_account_page.fill_create_new_customer_account_form(
        'Jane', 'Doe', 'janedoe0706@gmail.com', 'Janedoe123@', 'Janedoe123@'
    )
    create_customer_account_page.scroll_to_element(loc.user_already_exist_error_loc)
    create_customer_account_page.check_the_text(
        'There is already an account with this email address. '
        'If you are sure that it is your email address, click here to get your password and access your account.',
        loc.user_already_exist_error_loc
    )

def test_check_validation_when_password_and_confirm_password_values_arent_the_same(create_customer_account_page):
    create_customer_account_page.open_page()
    create_customer_account_page.fill_create_new_customer_account_form(
        'Jane', 'Doe', 'janedoe0706@gmail.com', 'Janedoe123@', 'Janedoe12345'
    )
    create_customer_account_page.scroll_to_element(loc.confirm_password_isnt_the_same_text)
    create_customer_account_page.check_the_text(
        'Please enter the same value again.',
        loc.confirm_password_isnt_the_same_text
    )

def test_check_validation_when_any_required_field_is_empty(create_customer_account_page):
    create_customer_account_page.open_page()
    create_customer_account_page.fill_create_new_customer_account_form(
        '', 'Doe', 'janedoe0706@gmail.com', 'Janedoe123@', 'Janedoe123@'
    )
    create_customer_account_page.scroll_to_element(loc.required_field_text)
    create_customer_account_page.check_the_text(
        'This is a required field.',
        loc.required_field_text
    )
