from pages.base_page import BasePage
from pages.locators import create_customer_account_locators_page as loc


class CreateCustomerAccount(BasePage):
    page_url = '/customer/account/create/'


    def fill_create_new_customer_account_form(self,
                                              firstname,
                                              lastname,
                                              email,
                                              password,
                                              confirm_password):
        # Data using for the CreateCustomerAccount form
        first_name_field = self.find(loc.first_name_field_loc)
        last_name_field = self.find(loc.last_name_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        confirm_password_field = self.find(loc.confirm_password_field_loc)
        create_account_btn = self.find(loc.create_account_btn_loc)

        first_name_field.send_keys(firstname)
        last_name_field.send_keys(lastname)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(confirm_password)
        create_account_btn.click()

    def check_email_already_used_text(self, text):
        self.scroll_to_element(locator=loc.user_already_exist_error_loc)
        self.check_the_text(text=text, locator=loc.user_already_exist_error_loc)


    def check_passwords_arent_the_same_text(self, text):
        self.scroll_to_element(locator=loc.confirm_password_isnt_the_same_text)
        self.check_the_text(text=text, locator=loc.confirm_password_isnt_the_same_text)


    def check_required_field_is_empty_text(self, text):
        self.scroll_to_element(locator=loc.required_field_text)
        self.check_the_text(text=text, locator=loc.required_field_text)
