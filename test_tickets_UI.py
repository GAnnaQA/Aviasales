from pages.main_page_tickets import main_page_of_search_tickets


def test_choose_popular_destination(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    aviasales.choose_country_of_location()
    aviasales.add_coockie()
    popular_destination = aviasales.choose_popular_destination(3)
    selected_destination = aviasales.get_destination_value()
    assert popular_destination == selected_destination