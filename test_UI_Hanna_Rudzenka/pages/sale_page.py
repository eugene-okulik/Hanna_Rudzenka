from playwright.sync_api import expect
from test_UI_Hanna_Rudzenka.pages.base_page import BasePage

CATEGORY_MENU_TITLES_LOC = "div.categories-menu>strong.title"
BLOCK_PROMO_ELEMS_LOC = "a.block-promo"


class SalePage(BasePage):
    page_endpoint = '/sale.html'

    def check_category_menu_titles_are(self, title_list: list):
        categoty_title_list = [elem.text_content().upper() for elem in self.find(CATEGORY_MENU_TITLES_LOC).element_handles()]
        assert categoty_title_list == title_list

    def check_block_promo_elems_count_is(self, count):
        expect(self.find(BLOCK_PROMO_ELEMS_LOC)).to_have_count(count)
