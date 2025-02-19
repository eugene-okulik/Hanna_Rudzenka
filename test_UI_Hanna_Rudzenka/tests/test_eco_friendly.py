
def test_sale_page_is_open(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.check_page_endpoint_is_correct()
    eco_friendly.check_page_title_is('Eco Friendly')


def test_sort_by_price(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.select_by_value('price')
    eco_friendly.check_sort_by_price()


def test_sort_by_name(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.select_by_value('name')
    eco_friendly.check_sort_by_product_name()
