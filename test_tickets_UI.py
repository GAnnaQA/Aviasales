from pages.main_page_tickets import main_page_of_search_tickets
from pages.data import data_test


def test_choose_popular_destination(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    popular_destination = aviasales.choose_popular_destination(3)
    selected_destination = aviasales.get_destination_value()
    assert popular_destination == selected_destination


def test_choose_date(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    aviasales.choose_date_of_departure(data_test.serch_month, data_test.serch_day)
    aviasales.choose_one_way_tickets()
    departure_date_value = aviasales.get_departure_date_value()
    return_date_value = aviasales.get_return_date_value()
    assert data_test.serch_day in departure_date_value
    assert return_date_value == 'Return'


def test_choose_count_of_passenger(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    passengers_value = aviasales.choose_count_of_passenger(
        data_test.adults_count, data_test.children_count, data_test.infants_count
        )
    assert data_test.sum_count_passengers in passengers_value
    