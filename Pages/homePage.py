import time

from .basePage import BasePage
from  selenium.webdriver.common.by import By

class HomePage(BasePage):
    search_box = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    Search_Button = (By.ID, "nav-search-submit-button")

    def search_products(self , product_name):
        self.clear(self.search_box)
        self.send_keys(self.search_box, product_name)
        time.sleep(5)

        self.click(self.Search_Button)
        time.sleep(5)