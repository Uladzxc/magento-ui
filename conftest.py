import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_customer_account_page import CreateCustomerAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale
import tempfile


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument(f'--user-data-dir={tempfile.mkdtemp()}')

    chrome_driver = webdriver.Chrome(options=options)
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
