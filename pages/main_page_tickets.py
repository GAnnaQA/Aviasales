from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

class main_page_of_search_tickets:
    def __init__(self, browser: WebDriver):
        self._driver = browser
        self._driver.get("https://www.aviasales.ru")

    def choose_country_of_location(self):
        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'div.s__Pu31UB5yQr0c21xBwtm7.s__ZacA4gC79hOijYojmhjk'
            )))
            choose_button = self._driver.find_element(
                By.XPATH,
                "//button[@data-test-id='button' and .//div[text()='Сохранить']]"
            )
            choose_button.click()
        except (NoSuchElementException, TimeoutException):
            print("Элемент не найден, продолжаем выполнение теста.")
    
    def add_coockie(self):
        policy = {
            'name': 'cookies_policy',
            'value': '%7B%22accepted%22%3Atrue%2C%22technical%22%3Atrue%2C%22marketing%22%3Atrue%7D'
        }
        self._driver.add_cookie(policy)
        self._driver.refresh()