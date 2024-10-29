from pages.main_page_tickets import main_page_of_search_tickets


def test_test(add_driver):
    aviasales = main_page_of_search_tickets(add_driver)
    aviasales.choose_country_of_location()
    aviasales.add_coockie()