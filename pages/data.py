from datetime import datetime, timedelta, timezone
import random
import allure

@allure.step('Обращение к хранилищу данных')
class data_test:
    Economy_class = "Economy"
    Comfort_class = "Comfort"
    Business_class = "Business"
    First_class = "First"
    with allure.step('Генерция номера популярного направления для выбора'):
        direction_number = random.randint(1, 4)
    with allure.step('Случайный выбор дня'):
        serch_day = random.randint(1, 28)
    
    @allure.step('Случайный выбор месяца')
    def choose_month(self)-> str:
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
        serch_month = random.choice(months)
        return serch_month
    
    @allure.step('Генерация количества пассажиров')
    def generate_passenger_count(self)-> list[str]:
        max_passengers = 9 
        adults = random.randint(1, max_passengers)
        max_children_and_infants = max_passengers - adults
        if max_children_and_infants > 0:
            children = random.randint(0, max_children_and_infants)
            infants = random.randint(0, min(adults, max_children_and_infants - children))
        else:
            children = 0
            infants = 0
        sum_count_passengers = adults + children + infants
        return [str(adults), str(children), str(infants), str(sum_count_passengers)]