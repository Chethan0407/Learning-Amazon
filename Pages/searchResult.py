from .basePage import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, "[data-component-type='s-search-result'] h2 a")

    PRODUCT_TITLES = (By.CSS_SELECTOR, "[data-component-type='s-search-result'] h2 a")




    def assert_atlest_three_products(self):
        product_titles = self.get_product_titles()
        assert len(product_titles) >=3, "less than three products found"
        return product_titles[:3]

    def get_product_titles(self):
        elements = self.find_elements(self.PRODUCT_TITLES)
        return [element.text for element in elements[:3]]








