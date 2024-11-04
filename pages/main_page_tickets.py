from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import allure

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

    def choose_popular_destination(self, index: int)-> str:
        if not (1 <= index <= 4):
            raise ValueError("Индекс должен быть от 1 до 4")
        popular_destinations_block = self._driver.find_element(
            By.CSS_SELECTOR,'div[data-test-id="popular-destinations"]'
            )
        popular_destinations = popular_destinations_block.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="collection-slider"]'
            )
        popular_destination = popular_destinations.find_element(
            By.CSS_SELECTOR, f'ul.s__oBcz7qdm90uD5MSw0BKH li:nth-child({index})'
            )
        button = popular_destination.find_element(
            By.CSS_SELECTOR, 'button.s__KWPoGkACMTpTVMBdnFfA'
            )
        figure = button.find_element(
            By.CSS_SELECTOR, 'figure[data-test-id="poi-item"]'
            )
        title_value = figure.find_element(
            By.CSS_SELECTOR, 'figcaption.s__mCrQRSF2YRRJThmoLCfJ'
            ).get_attribute('title')
        button.click()
        return title_value
    
    def get_destination_value(self)-> str:
        try:
            input_element = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 'input[data-test-id="destination-input"]'
                    ))
            )
            destination_value = input_element.get_attribute('value')
            return destination_value
        except TimeoutException:
            print("Время ожидания истекло: элемент не найден.")
            return "Элемент не найден"