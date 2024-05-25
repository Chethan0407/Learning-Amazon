from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException





class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
       element =  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
       element.click()

    def clear(self, locator):
        self.find_element(locator).clear()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_for_element_is_visible(self, locator, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(EC
                                                      .visibility_of_element_located(locator))

        except TimeoutException:
            print(f"element {locator} is nit visibke in {timeout} seconds")



