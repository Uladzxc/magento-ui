from pages.base_page import BasePage
from pages.locators import eco_friendly_locators_page as loc
from selenium.webdriver.support.ui import Select



class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def select_view(self, view_type: str):
        if view_type == "grid":
            view_btn = self.wait.until(self.ec.element_to_be_clickable(loc.grid_btn))
        elif view_type == "list":
            view_btn = self.wait.until(self.ec.element_to_be_clickable(loc.list_btn))
        else:
            raise ValueError("view_type must be 'grid' or 'list'")

        view_btn.click()
        return view_btn

    def assert_display_type(self, view_type: str, expected_display: str):
        if view_type == "grid":
            container = self.wait.until(self.ec.presence_of_element_located(loc.grid_container))
        elif view_type == "list":
            container = self.wait.until(self.ec.presence_of_element_located(loc.list_container))
        else:
            raise ValueError("view_type must be 'grid' or 'list'")

        actual_display = self.driver.execute_script(
            "return window.getComputedStyle(arguments[0]).display;", container
        )

        assert actual_display == expected_display, (
            f"Expected display: '{expected_display}' for view '{view_type}', but got: '{actual_display}'"
        )

        return actual_display

    def select_element_from_the_dropdown_and_check_items_display(self, text):
        # Select the dropdown value
        dropdown = self.find(loc.dropdown_list)
        select = Select(dropdown)
        select.select_by_visible_text(text)

        # Click the sorter button
        sorter_btn = self.scroll_to_element(loc.sorter_btn)
        sorter_btn.click()

        # Wait while the first item is displayed
        self.wait_until_the_element_is_clickable(loc.first_item)

        item_1 = self.find(loc.first_product)
        item_2 = self.find(loc.second_product)

        # Get prices in text type
        price_text_1 = item_1.text
        price_text_2 = item_2.text

        # Convert prices from string to float type
        price_value_1 = float(price_text_1.replace("$", "").strip())
        price_value_2 = float(price_text_2.replace("$", "").strip())

        # Check the selected sorting
        sorter_btn_title = self.get_attribute(loc.sorter_btn, "title")

        if sorter_btn_title == "Set Descending Direction":
            assert price_value_1 < price_value_2, "Expected ascending order, but got descending."
        elif sorter_btn_title == "Set Ascending Direction":
            assert price_value_1 > price_value_2, "Expected descending order, but got ascending."
        else:
            raise ValueError(f"Unexpected sorter title: {sorter_btn_title}")
