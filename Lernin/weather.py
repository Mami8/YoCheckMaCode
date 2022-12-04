import datetime
import requests

api_key = open("appid.txt", "r").read()


def get_geocode(city="Afşin", country_code="TR"):
    """Returns geocode information of a given country

    Args:
        city (str, optional): Name of the country. Defaults to "Afşin".
        country_code (str, optional): Country code. Defaults to "TR".

    Returns:
        tuple: returns the lat and lon values of the country to be used in get_weather function
    """
    base_url_geocode = "http://api.openweathermap.org/geo/1.0/direct?"
    url_geocode = base_url_geocode + "appid=" + api_key + "&q=" + "Afşin,TR"
    
    response = requests.get(url_geocode).json()
    lat, lon = response[0]["lat"], response[0]["lon"]
    return lat, lon


def get_weather(lat, lon, appid=api_key):
    """Used to get weather data of a specific country

    Args:
        lat (float): The lat value of geo code. Comes from get_geocode function
        lon (float): The lon value of geo code. Comes from get_geocode function
        appid (str, optional): The API key of user. Get your's from OpenWheather. Defaults to api_key.

    Returns:
        tuple: Description of weather and temperature
    """
    base_url_weather = "https://api.openweathermap.org/data/2.5/weather?"
    url_weather = base_url_weather + "appid=" + api_key + "&lat=" + str(lat) + "&lon=" + str(lon) + "&lang=" + "tr" + "&units=" + "metric"
    response = requests.get(url_weather).json()
    
    description = response["weather"][0]["description"]
    temperature = response["main"]["temp"]
    return description, temperature
