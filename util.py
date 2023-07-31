import requests
import re
from dateutil import tz
from datetime import datetime


def get_current_time(city):
    cityname = f"America/{city}"
    timezone = tz.gettz(cityname)
    current_time = datetime.now(timezone)
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')


def get_weather_info(city):
    url = f"https://wttr.in/{city}?m1"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch weather information for {city}"


def get_Airport(city):
    city = city.replace("_", " ")
    pattern = fr'.*{re.escape(city)};United States'
    # patternFirstLine = r"^(Airport Code;Airport Name;City Name;Country Name;)"

    # Initialize a list to store the matches
    airports = []

    # Read the content of the text file line by line
    with open('airports-code.csv', 'r') as file:
        for line in file:
            # Search for the pattern in each line
            matches = re.findall(pattern, line)
            airports.extend(matches)
    return airports


def getCityInput():
    '''
    Part of Util Package

    Return:
    String for city name.
    '''
    return input("City Name: ")


def formatCityInput(cityname):
    return cityname.title().replace(" ", "_")


def formatLine(numberOfLines):
    '''
    Format output with empty lines printed to console

    Parameter:
    numberOfLines: Number of lines
    '''
    for i in range(numberOfLines):
        print()
