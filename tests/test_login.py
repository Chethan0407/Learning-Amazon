import time

import pytest
from Pages.loginPAge import Loginpage
from config_reader import read_configuration
import allure

@pytest.mark.usefixtures("driver")

class TestLogin:
    @allure.feature('Login Feature')
    @allure.story('User Login to Amazon')

    def test_login(self, driver):
       email = read_configuration('Default', 'Email')
       password = read_configuration('Default', 'Password')

       loginpage = Loginpage(driver)
       loginpage.click_signin()
       loginpage.enter_email(email)
       loginpage.enter_pass_and_submit(password)

