from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.ec = ec

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def get_attribute(self, locator: tuple, attribute_name: str) -> str:
        element = self.find(locator)
        return element.get_attribute(attribute_name)


    def check_the_text(self, text, locator):
        error_alert = self.driver.find_element(*locator)
        assert text == error_alert.text

    def scroll_to_element(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element
        )
        return element

    def wait_until_the_element_is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))
