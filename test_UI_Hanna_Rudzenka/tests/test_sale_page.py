
def test_sale_page_is_open(sale):
    sale.open_page()
    sale.check_page_endpoint_is_correct()
    sale.check_page_title_is('Sale')


def test_category_menu_titles(sale):
    sale.open_page()
    sale.check_category_menu_titles_are(["WOMEN'S DEALS", "MENS'S DEALS", 'GEAR DEALS'])


def test_block_promo_elems_length(sale):
    sale.open_page()
    sale.check_block_promo_elems_count_is(6)
