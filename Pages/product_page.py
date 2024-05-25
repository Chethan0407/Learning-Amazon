from .basePage import BasePage
from selenium.webdriver.common.by import By


class Product(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "a-autoid-1-announce")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)