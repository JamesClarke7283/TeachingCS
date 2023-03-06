"""
Step 1: Query Location https://openweathermap.org/find?q=[location]
Step 2: Get Locations from Query
"""

import requests
from bs4 import BeautifulSoup
import json

def get_locations(location):
    """Gets locations from query

    :param location: Location to query
    :return: List of locations
    """
    url = f"https://openweathermap.org/data/2.5/find?callback=?&q={location}&type=like&sort=population&cnt=30&appid=439d4b804bc8187953eb36d2a8c26a02"
    response = requests.get(url)
    json_str = response.text.lstrip("?(").rstrip(")")
    locations = json.loads(json_str)
    return locations


lst = get_locations("Texas")
print(lst)
