import time

from .basePage import  BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_ICON = (By.ID, "nav-cart-count-container")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//input[@name='proceedToRetailCheckout']")

    def click_cart_icon(self):
        self.click(self.CART_ICON)
        time.sleep(10)

    def proceed_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)


