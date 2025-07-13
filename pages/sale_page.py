from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class Sale(BasePage):
    page_url = '/sale.html'

    def check_if_deal_titles_are_correct(self,
                                         womens_text,
                                         mens_text,
                                         gears_text):
        womens = self.find(loc.womens_deals_loc)
        mens = self.find(loc.mens_deals_loc)
        gears = self.find(loc.gear_deals_loc)

        assert womens.text == womens_text, f"Expected '{womens_text}', but got '{womens.text}'"
        assert mens.text == mens_text, f"Expected '{mens_text}', but got '{mens.text}'"
        assert gears.text == gears_text, f"Expected '{gears_text}', but got '{gears.text}'"

    def check_the_sale_page_header_text(self, text):
        self.check_the_text(text=text, locator=loc.sale_page_title_loc)

    def check_the_shipping_info_text(self, text):
        self.scroll_to_element(locator=loc.shipping_is_free_loc)
        self.check_the_text(text=text, locator=loc.shipping_is_free_loc)