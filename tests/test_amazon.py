import time

import pytest
from Pages.homePage import HomePage
from  Pages.cartPage import CartPage
from Pages.product_page import Product
from Pages.searchResult import SearchResultPage
import allure

@pytest.mark.usefixtures("driver")


@allure.feature('Amazon Feature')
@allure.story('Search and Add to Cart')

class TestAmazon:
    def test_search_and_add_to_cart(self, driver):
        homepage = HomePage(driver)
        search_result_page = SearchResultPage(driver)
        product_page = Product(driver)
        cart_page = CartPage(driver)


        homepage.search_products("iphone")
        product_title = search_result_page.assert_atlest_three_products()

        #printing the first three products
        for title in product_title:
            print(title)
        print("have give 3 list of apple iphones")


        #click the first produuct and to add

        product_page.add_to_cart()
        time.sleep(5)
        cart_page.click_cart_icon()
        cart_page.proceed_checkout()







