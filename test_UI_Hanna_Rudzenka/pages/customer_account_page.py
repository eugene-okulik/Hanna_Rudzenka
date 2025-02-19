from playwright.sync_api import expect
from test_UI_Hanna_Rudzenka.pages.base_page import BasePage

SUCCESS_CREATE_MSG_LOC = '//*[@id="maincontent"]/div[1]/div[2]/div/div/div'


class CustomerAccount(BasePage):
    page_endpoint = '/customer/account/'

    def check_success_create_msg_is(self, text):
        expect(self.find(SUCCESS_CREATE_MSG_LOC).first).to_have_text(text)
