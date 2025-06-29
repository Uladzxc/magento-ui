from selenium.webdriver.common.by import By

# Grid locators
grid_btn = (By.XPATH, '(//strong[@data-value="grid"])[1]')
grid_container = (By.XPATH, '//div[@class="products wrapper grid products-grid"]')


# List locators
list_btn = (By.XPATH, '//a[@id = "mode-list"]')
list_container = (By.XPATH, '//div[@class="products wrapper list products-list"]')

# Item locators
first_item = (By.XPATH, '(//div[@class="product details product-item-details"])[1]')
first_item_size = (By.XPATH, '(//div[@class="swatch-option text"])[1]')
first_item_color = (By.XPATH, '(//div[@id="option-label-color-93-item-49"])[1]')


# Dropdown list
dropdown_list = (By.XPATH, '//select[@id="sorter"]')
sorter_btn = (By.XPATH, '//a[@data-role="direction-switcher"]')

# Items on the page
first_product = (By.XPATH, '(//span[@class="price"])[1]')
second_product = (By.XPATH, '(//span[@class="price"])[2]')

