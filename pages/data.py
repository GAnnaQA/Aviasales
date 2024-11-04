from datetime import datetime, timedelta, timezone
import random


class data_test:
    serch_day = '4'
    serch_month = 'April'
    adults_count = '3'
    children_count = '2'
    infants_count = adults_count
    sum_count_passengers = str(int(adults_count) + int(children_count) + int(infants_count))