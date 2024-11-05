from pages.main_page_tickets import main_page_of_search_tickets
from pages.data import data_test
from time import sleep
import allure

@allure.id("Positive4")
@allure.feature('Search')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Позитивный тест на поиск авиабилетов в одну сторону')
def test_input(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    aviasales.enter_place_of_destination('Mosc')
    destination_place = aviasales.get_destination_value()
    aviasales.clear_departure_place_input()
    aviasales.enter_place_of_departure('New')
    departure_place = aviasales.get_departure_place_value()


@allure.id("Positive1")
@allure.feature('Search')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Позитивный тест на поиск авиабилетов в разделе Популярные направления')
def test_choose_popular_destination(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    data = data_test()
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    popular_destination = aviasales.choose_popular_destination(data.direction_number)
    selected_destination = aviasales.get_destination_value()
    with allure.step('Проверка отображения наименования выбранного направления в поле ввода "To"'):
        assert popular_destination == selected_destination


@allure.id("Positive2")
@allure.feature('Search')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Позитивный тест на ввод и отображение валидной даты отправления')
def test_choose_date(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    data = data_test()
    day = data.serch_day
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    aviasales.choose_date_of_departure(data.choose_month(), day)
    aviasales.choose_one_way_tickets()
    departure_date_value = aviasales.get_departure_date_value()
    return_date_value = aviasales.get_return_date_value()
    with allure.step('Проверка отображения выбранного дня вылета в поле ввода "Departure"'):
        assert str(day) in departure_date_value
    with allure.step('Проверка незаполненности поля ввода "Return"'):
        assert return_date_value == 'Return'


@allure.id("Positive3")
@allure.feature('Search')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Позитивный тест на выбор и отображение количества пассажиров')
def test_choose_count_of_passenger(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    data = data_test()
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    passengers = data.generate_passenger_count()
    passengers_value = aviasales.choose_count_of_passenger(
        passengers[0], passengers[1], passengers[2]
        )
    with allure.step('Проверка отображения выбранного количества пассажиров в поисковой строке'):
        assert passengers[3] in passengers_value
