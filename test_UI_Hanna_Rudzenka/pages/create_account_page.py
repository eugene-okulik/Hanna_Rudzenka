from playwright.sync_api import expect
from test_UI_Hanna_Rudzenka.pages.base_page import BasePage

FIRST_NAME_LOC = "input[name = 'firstname']"
LAST_NAME_LOC = "input[name = 'lastname']"
EMAIL_LOC = "input[name = 'email']"
PASSWORD_LOC = "input[name = 'password']"
PASSWORD_CONFIRM_LOC = "input[name = 'password_confirmation']"
CREATE_ACCOUNT_BTN_LOC = "[title = 'Create an Account']"
EMPTY_FIELD_ERROR_LOC = "//*[text()='This is a required field.']"
PASSWORD_CONFIRM_ERROR_LOC = "div#password-confirmation-error"


class CreateAccount(BasePage):
    page_endpoint = '/customer/account/create/'

    def fill_in_form(self, first_name, last_name, email, password, password_confirm):
        self.find(FIRST_NAME_LOC).fill(first_name)
        self.find(LAST_NAME_LOC).fill(last_name)
        self.find(EMAIL_LOC).fill(email)
        self.find(PASSWORD_LOC).fill(password)
        self.find(PASSWORD_CONFIRM_LOC).fill(password_confirm)
        self.click(CREATE_ACCOUNT_BTN_LOC)

    def click_account_button(self):
        self.click(CREATE_ACCOUNT_BTN_LOC)

    def check_empty_field_messages_count_is(self, count):
        expect(self.find(EMPTY_FIELD_ERROR_LOC)).to_have_count(count)

    def check_password_confirm_error_msg_is(self, text):
        expect(self.find(PASSWORD_CONFIRM_ERROR_LOC)).to_have_text(text)
