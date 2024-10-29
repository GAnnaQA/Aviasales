import pytest
from selenium import webdriver


@pytest.fixture
def add_driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4) 
    browser.maximize_window()

    yield browser 

    browser.quit()