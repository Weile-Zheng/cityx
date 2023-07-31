import requests
import pytz
from datetime import datetime


def get_current_time(city):
    cityname = f"America/{city}"
    timezone = pytz.timezone(cityname)
    current_time = datetime.now(timezone)
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')


def get_weather_info(city):
    url = f"https://wttr.in/{city}?m1"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch weather information for {city}"


def getCityInput():
    '''
    Part of Util Package

    Return:
    String for city name.
    '''
    return input("City Name: ")


def formatCityInput(cityname):
    return cityname.title().replace(" ", "_")
