from selenium.webdriver.common.by import By


# Page title locator
sale_page_title_loc = (By.XPATH, "//span[@class='base']")

# Deal section title locators
womens_deals_loc = (By.XPATH, "//span[text()=\"Women's Deals\"]")
mens_deals_loc = (By.XPATH, "//span[text()=\"Mens's Deals\"]")
gear_deals_loc = (By.XPATH, "//span[text()='Gear Deals']")

# Shipping is free information locator
shipping_is_free_loc = (By.XPATH, "//strong[contains(text(), 'Spend $50 or more')]")

