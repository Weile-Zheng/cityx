from util import *
import os
GREEN = '\033[32m'
RESET = '\033[0m'


def generateToConsole(city):
    formatLine(5)
    print(f'Current time: {get_current_time(city)}')
    formatLine(5)

    # To be inputted into File.txt
    print(get_weather_info(city))
    airports = get_Airport(city)
    if len(airports) == 0:
        print("No Commercial Airportx at this City")
    print("\nCity Airports")
    print("Airport Code | Airport Name | City Name | Country Name ")
    for i in airports:
        print(f'- {i.replace(";", " | ")}')
    formatLine(5)
    print(GREEN+"Guide Generated"+RESET)


def generateToFile(city):
    currentTime = get_current_time(city)
    weather = get_weather_info(city)
    airports = get_Airport(city)

    fileName = f'~/cityx/userFiles/{city}'
    expanded_file_name = os.path.expanduser(fileName)
    try:
        with open(expanded_file_name, 'x') as file:
            file.write(f'Current time at {city}: {currentTime}\n')
            file.write(weather+"\n")
            file.write(
                "Airport Code | Airport Name | City Name | Country Name ")
            if len(airports) == 0:
                file.write("No airports at this city \n")
            else:
                for lines in airports:
                    file.write(lines.replace(";", " | ")+"\n")
                    file.write(getFlightLine(city))
            print(GREEN+"Guide Generated"+RESET)
    except FileExistsError:
        print(
            f"Guide for: {city} already created. Please use the view option instead")
