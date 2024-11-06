from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import allure


@allure.story('Поиск авиабилетов (UI)')
class main_page_of_search_tickets:
    @allure.step('Открыть главную страницу сайта Авиасейлс')
    def __init__(self, browser: WebDriver):
        self._driver = browser
        self._driver.get("https://www.aviasales.ru")


    @allure.step('Настрайка местоположения')
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


    @allure.step('Установка cookies_policy')
    def add_coockie(self):
        policy = {
            'name': 'cookies_policy',
            'value': '%7B%22accepted%22%3Atrue%2C%22technical%22%3Atrue%2C%22marketing%22%3Atrue%7D'
        }
        self._driver.add_cookie(policy)
        self._driver.refresh()


    @allure.step('Ввести значение в поле ввода "From"')
    def enter_place_of_departure(self, DeparturePlace: str):
        departure_input = self._driver.find_element(
            By.CSS_SELECTOR, 'input[data-test-id="origin-input"]'
            )
        departure_input.send_keys(DeparturePlace)
        dropdown = self._driver.find_element(By.CSS_SELECTOR, 'div[data-test-id="dropdown"]')
        city = dropdown.find_element(By.CSS_SELECTOR, ":first-child")
        city.click()
        

    @allure.step('Получить значение поля ввода "From"')
    def get_departure_place_value(self)-> str:
        departure_input = self._driver.find_element(
            By.CSS_SELECTOR, 'input[data-test-id="origin-input"]'
            )
        return departure_input.get_attribute('value')
    

    @allure.step('Очистить поле ввода "From"')
    def clear_departure_place_input(self):
        departure_input = self._driver.find_element(
            By.CSS_SELECTOR, 'input[data-test-id="origin-input"]'
            )
        departure_input.clear()


    @allure.step('Ввести значение в поле ввода "To"')
    def enter_place_of_destination(self, DestinationPlace: str):
        destination_input = self._driver.find_element(
            By.CSS_SELECTOR, 'input[data-test-id="destination-input"]'
            )
        destination_input.send_keys(DestinationPlace)
        dropdown = self._driver.find_element(By.CSS_SELECTOR, 'div[data-test-id="dropdown"]')
        city = dropdown.find_element(By.CSS_SELECTOR, ":first-child")
        city.click()
        

    @allure.step('Получить значение поля ввода "To"')
    def get_destination_value(self)-> str:
        destination_input = self._driver.find_element(
            By.CSS_SELECTOR, 'input[data-test-id="destination-input"]'
            )
        return destination_input.get_attribute('value')
    

    @allure.step('Очистить поле ввода "To"')
    def clear_destination_input(self):
        destination_input = self._driver.find_element(
            By.CSS_SELECTOR, 'input[data-test-id="destination-input"]'
            )
        destination_input.clear()


    @allure.step('Ввод даты вылета в поле "Departure"')
    def enter_date_of_departure(self, StartDate: str)-> str:
        self._driver.find_element(
                    By.CSS_SELECTOR, 'button[data-test-id="start-date-field"]'
                    ).click()
        while True:
            try:
                serch_date = self._driver.find_element(
                    By.CSS_SELECTOR, f'div[data-test-id="date-{StartDate}"]'
                    )
                serch_date.click()
                break
            except NoSuchElementException:
                buttons = self._driver.find_elements(
                    By.CSS_SELECTOR, 'button[data-test-id="button"]'
                    )
                if len(buttons) > 1:
                    buttons[1].click()
                else:
                    print("Кнопка с индексом 1 не найдена.")
                    break
        return serch_date.text


    @allure.step('Получения значения, отображаемого в поле "Departure"')
    def get_departure_date_value(self)-> str:
        button = self._driver.find_element(
            By.CSS_SELECTOR,'button[data-test-id="start-date-field"]'
            )
        div = button.find_element(
            By.CSS_SELECTOR, 'div.s__Ri8DaLigC3WqN5MS5LyK'
            )
        departure_date_value = div.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="start-date-value"]'
            ).text
        return departure_date_value
    

    @allure.step('Ввод даты обратного билета в поле "Return"')
    def enter_date_of_return(self, ReturnDate: str)-> str:
        self._driver.find_element(
            By.CSS_SELECTOR,'button[data-test-id="end-date-field"]'
            ).click()
        while True:
            try:
                serch_date = self._driver.find_element(
                    By.CSS_SELECTOR, f'div[data-test-id="date-{ReturnDate}"]'
                    )
                serch_date.click()
                break
            except NoSuchElementException:
                buttons = self._driver.find_elements(
                    By.CSS_SELECTOR, 'button[data-test-id="button"]'
                    )
                if len(buttons) > 1:
                    buttons[1].click()
                else:
                    print("Кнопка с индексом 1 не найдена.")
                    break
        return serch_date.text if 'serch_date' in locals() else "Элемент не найден."
        

    @allure.step('Получения значения, отображаемого в поле "Return"')
    def get_return_date_value(self)-> str:
        button = self._driver.find_element(
            By.CSS_SELECTOR,'button[data-test-id="end-date-field"]'
            )
        div = button.find_element(
            By.CSS_SELECTOR, 'div.s__Ri8DaLigC3WqN5MS5LyK'
            )
        return_date_value = div.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="end-date-value"]'
            ).text
        return return_date_value


    @allure.step('Нажатие на кнопку "I don`t need a return ticket"')
    def choose_one_way_tickets(self)-> None|str:
        try:
            dont_need_return_ticket_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//button[@data-test-id='calendar-action-button' and contains(., 'I don’t need a return ticket')]"
                ))
                )
            dont_need_return_ticket_button.click()
        except (TimeoutException, NoSuchElementException):
            return "Кнопка не отображается на странице"


    @allure.step('Установка количества пассажиров')
    def choose_count_of_passenger(self, Adults: str, Children: str, Infants: str):
        button = self._driver.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="passengers-field"]'
            )
        button.click()
        adults_value = self._driver.find_element(
            By.XPATH, '//div[@data-test-id="number-of-adults"]//div[@data-test-id="passenger-number"]'
            ).text
        while adults_value != Adults:
            if adults_value < Adults:
                self._driver.find_element(
                    By.XPATH, '//div[@data-test-id="number-of-adults"]//button[@data-test-id="increase-button"]'
                ).click()
            elif adults_value > Adults:
                self._driver.find_element(
                    By.XPATH, '//div[@data-test-id="number-of-adults"]//button[@data-test-id="decrease-button"]'
                ).click()
            adults_value = self._driver.find_element(
                By.XPATH, '//div[@data-test-id="number-of-adults"]//div[@data-test-id="passenger-number"]'
                ).text
        children_value = self._driver.find_element(
            By.XPATH, '//div[@data-test-id="number-of-children"]//div[@data-test-id="passenger-number"]'
            ).text
        while children_value != Children:
            if children_value < Children:
                self._driver.find_element(
                    By.XPATH, '//div[@data-test-id="number-of-children"]//button[@data-test-id="increase-button"]'
                ).click()
            elif children_value > Children:
                self._driver.find_element(
                    By.XPATH, '//div[@data-test-id="number-of-children"]//button[@data-test-id="decrease-button"]'
                ).click()
            children_value = self._driver.find_element(
                By.XPATH, '//div[@data-test-id="number-of-children"]//div[@data-test-id="passenger-number"]'
                ).text
        infants_value = self._driver.find_element(
            By.XPATH, '//div[@data-test-id="number-of-infants"]//div[@data-test-id="passenger-number"]'
            ).text
        while infants_value != Infants:
            if infants_value < Infants:
                self._driver.find_element(
                    By.XPATH, '//div[@data-test-id="number-of-infants"]//button[@data-test-id="increase-button"]'
                ).click()
            elif infants_value > Infants:
                self._driver.find_element(
                    By.XPATH, '//div[@data-test-id="number-of-infants"]//button[@data-test-id="decrease-button"]'
                ).click()
            infants_value = self._driver.find_element(
                By.XPATH, '//div[@data-test-id="number-of-infants"]//div[@data-test-id="passenger-number"]'
                ).text
        button.click()
    
    @allure.step('Получение значения количества пассажиров, отображаемого в поисковой строке')
    def get_passengers_count_value(self):
        button = self._driver.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="passengers-field"]'
            )
        return button.find_element(
            By.CSS_SELECTOR, 'div[data-test-id="passenger-numbers"]'
            ).text
        

    @allure.step('Выбор страны в разделе "Популярные направления"')
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
    

    @allure.step('Получения значения, отображаемого в поле "To"')
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


    @allure.step('Установка класса билета')
    def choose_class(self, Class):
        button = self._driver.find_element(
            By.CSS_SELECTOR, 'button[data-test-id="passengers-field"]'
            )
        button.click()
        radiobutton = self._driver.find_element(
            By.XPATH, f'//label[@data-test-id="radio-button" and .//span[text()="{Class}"]]'
            )
        radiobutton.click()
        button.click()

    @allure.step('Получение значения класса, отображаемого в поисковой строке')
    def get_class_value(self):
        return self._driver.find_element(By.CSS_SELECTOR, 'div[data-test-id="trip-class"]').text