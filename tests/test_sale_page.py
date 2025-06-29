from pages.locators import sale_page_locators as loc

def test_check_the_deal_titles(sale_page):
    sale_page.open_page()
    sale_page.check_if_deal_titles_are_correct(
        "Women's Deals",
        "Mens's Deals",
        "Gear Deals"
    )


def test_check_if_page_title_is_correct(sale_page):
    sale_page.open_page()
    sale_page.check_the_text(
        'Sale',
        loc.sale_page_title_loc)


def test_check_if_free_shipping_info_displays(sale_page):
    sale_page.open_page()
    sale_page.scroll_to_element(loc.shipping_is_free_loc)
    sale_page.check_the_text(
        'Spend $50 or more — shipping is free!',
        loc.shipping_is_free_loc)
