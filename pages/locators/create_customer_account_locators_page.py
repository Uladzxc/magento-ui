from selenium.webdriver.common.by import By


# Fields locators
first_name_field_loc = (By.XPATH, '//input[@title="First Name"]')
last_name_field_loc = (By.XPATH, '//input[@title="Last Name"]')
email_field_loc = (By.XPATH, '//input[@title="Email"]')
password_field_loc = (By.XPATH, '//input[@title="Password"]')
confirm_password_field_loc = (By.XPATH, '//input[@title="Confirm Password"]')

# Button locator
create_account_btn_loc = (By.XPATH, '//button[@title="Create an Account"]')

# User already exist error test
user_already_exist_error_loc = (By.XPATH, '//div[@role="alert"]')

# Password value doesn't match the ConfirmPassword value
confirm_password_isnt_the_same_text = (By.XPATH, '//div[@for="password-confirmation"]')

# Required fields validation text
required_field_text = (By.XPATH, '//div[text()="This is a required field."]')
