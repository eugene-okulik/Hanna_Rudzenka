from test_UI_Hanna_Rudzenka.pages.base_page import BasePage

SORTER_LOC = "#sorter"
PRICE_LIST_LOC = ".price-wrapper"
PRODUCT_LIST_LOC = "a.product-item-link"


class EcoFriendly(BasePage):
    page_endpoint = '/collections/eco-friendly.html'

    def select_by_value(self, value):
        self.page.evaluate(f"""
                const selectElement = document.querySelector('select#sorter');
                selectElement.value = '{value}';
                selectElement.dispatchEvent(new Event('change', {{ bubbles: true }}));
                window.location.href = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html?product_list_order={value}';
            """)
        self.page.wait_for_url(
            f'https://magento.softwaretestingboard.com{self.page_endpoint}?product_list_order={value}')

    def check_sort_by_price(self):
        price_elements = self.find(PRICE_LIST_LOC).element_handles()
        price_list = [float(price.text_content()[1:]) for price in price_elements]
        assert price_list == sorted(price_list)

    def check_sort_by_product_name(self):
        product_list_name = self.find(PRODUCT_LIST_LOC).element_handles()
        product_title_list = [product.text_content().strip() for product in product_list_name if
                              product.text_content().strip()]
        assert product_title_list == sorted(product_title_list)
