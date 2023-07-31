import requests
import re
import pytz
from dateutil import tz
from datetime import datetime


def get_current_time(city):
    current_time = datetime.now(getTimeZone(city))
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')


def getTimeZone(city):
    '''
    Depreciated: (For this program) No longer being use in this program for finding timezone

    This function is only used in partner with get_current_time(city). Use pytzTimeZone for finding TimeZone
    '''
    cityname = f"America/{city}"
    return tz.gettz(cityname)


def pytzTimeZone(city):
    '''

    '''
    # Pytz database use space for seperating city names.
    city = city.replace("_", " ")
    try:
        # Get the time zone using the city name
        timezone = pytz.timezone(city)
        return timezone
    except pytz.UnknownTimeZoneError:
        return None


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

    Return:
    lines: String of new line character 
    '''
    lines = ""
    for i in range(numberOfLines):
        lines += "\n"
    return lines
