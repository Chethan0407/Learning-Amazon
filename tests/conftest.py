import pytest
from selenium import webdriver
import configparser
import  allure
from config_reader import read_configuration



config = configparser.ConfigParser()
config.read('config.ini')


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="function")
def driver(request):
    global driver
    browser =  request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser =="firefox":
        driver = webdriver.Firefox()
    else:
        print("enter the valid browser name")

    base_url = read_configuration('Default', 'BaseURL')
    driver.get(base_url)
    yield driver
    driver.quit()




