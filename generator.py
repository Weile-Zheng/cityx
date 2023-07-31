from util import *
GREEN = '\033[32m'
RESET = '\033[0m'


def generate(city):
    formatLine(5)
    print(get_current_time(city))
    print(get_weather_info(city))
    airports = get_Airport(city)
    print("\nCity Airports")
    print("Airport Code | Airport Name | City Name | Country Name ")
    for i in airports:
        print(f'- {i.replace(";", " | ")}')
    formatLine(5)
    print(GREEN+"Guide Generated"+RESET)
