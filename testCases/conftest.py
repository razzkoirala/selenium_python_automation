import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver

# Reference: https://github.com/pavanoltraining/nopCommerceProject/blob/master/pageObjects/LoginPage.py