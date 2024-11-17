from pages.main_page_tickets import main_page_of_search_tickets
from pages.data import data_test
import allure


@allure.id("Smoke1")
@allure.feature('Search')
@allure.severity(allure.severity_level.BLOCKER)
@allure.title('Позитивный тест на поиск авиабилетов в одну сторону')
def test_serch_tickets(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    aviasales.enter_place_of_destination('Mosc')
    destination_place = aviasales.get_destination_value()
    aviasales.clear_departure_place_input()
    aviasales.enter_place_of_departure('New')
    departure_place = aviasales.get_departure_place_value()
    data = data_test()
    startDate = data.get_random_date()
    aviasales.enter_date_of_departure(startDate)
    aviasales.choose_one_way_tickets()
    aviasales.choose_count_of_passenger('2','1','1')
    aviasales.choose_class(data.Economy_class)
    aviasales.click_search_button()
    # number_of_ticket = data.ticket_number
    # data_about_ticket = aviasales.get_data_about_found_tickets(number_of_ticket)
    # assert data_about_ticket == departure_place

