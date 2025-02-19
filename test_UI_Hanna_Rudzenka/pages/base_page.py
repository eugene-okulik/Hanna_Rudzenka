import re
from playwright.sync_api import Page, Locator, expect


class BasePage:
    base_url = "https://magento.softwaretestingboard.com/"
    page_endpoint = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(f'{self.base_url}{self.page_endpoint}')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def click(self, locator):
        self.find(locator).click()

    def get_text(self, locator):
        return self.find(locator).text_content()

    def check_page_title_is(self, title):
        expect(self.page).to_have_title(title)

    def check_page_endpoint_is_correct(self):
        expect(self.page).to_have_url(re.compile(f".*{self.page_endpoint}.*"))
