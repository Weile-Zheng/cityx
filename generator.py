from util import *
GREEN = '\033[32m'
RESET = '\033[0m'


def generate(city):
    print(get_current_time(city))
    print(get_weather_info(city))
    airports = get_Airport(city)
    print("\nCity Airports")
    for i in airports:
        print(i.replace(" | ", " "))
    print(GREEN+"Guide Generated"+RESET)
