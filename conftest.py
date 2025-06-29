import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_customer_account_page import CreateCustomerAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale



@pytest.fixture()
def driver():
    options = Options()
    chrome_driver = webdriver.Chrome(options=options)
    # sleep(3)
    return chrome_driver


@pytest.fixture()
def create_customer_account_page(driver):
    return CreateCustomerAccount(driver)

@pytest.fixture()
def sale_page(driver):
    return Sale(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)
