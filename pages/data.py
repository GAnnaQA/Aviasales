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
    with allure.step('Генерция номера найденного билета'):
        ticket_number = random.randint(0, 9)
    
    @allure.step('Генерация даты')
    def get_random_date(self) -> str:
        current_date = datetime.now()
        random_days = random.randint(0, 330)
        random_date = current_date + timedelta(days=random_days)
        formatted_date = random_date.strftime("%d.%m.%Y")
        return formatted_date

    @allure.step('Генерация даты обратного билета')
    def get_return_date(self, startDate: str, daysCount: int) -> str:
        date_object = datetime.strptime(startDate, "%d.%m.%Y")
        return_date = date_object + timedelta(days=daysCount)
        formatted_date = return_date.strftime("%d.%m.%Y")
        return formatted_date

    
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