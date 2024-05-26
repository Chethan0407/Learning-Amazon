from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))


    def click(self, locator):
        try:
            element =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element.click()
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Error clicking element {locator}: {e}")


    def clear(self, locator):
        self.find_element(locator).clear()

    def send_keys(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element.send_keys(text)

        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"error sending keys to element {locator}: {e}")

    def wait_for_element_is_visible(self, locator, timeout = 10):
        try:
            WebDriverWait(self.driver, timeout).until(EC
                                                      .visibility_of_element_located(locator))

        except TimeoutException:
            print(f"element {locator} is nit visibke in {timeout} seconds")



