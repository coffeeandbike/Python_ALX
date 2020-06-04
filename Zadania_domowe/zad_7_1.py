"""
Zadanie 7.1 | Pobieranie informacji z API metaweather
​
Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
Skorzystaj z modułu urllib.request, json oraz API MetaWeather.
"""

import json
import urllib.request
from urllib.request import Request

location = input("Enter Location as WOEID (Where On Earth IDentifier): ")

url = f'https://www.metaweather.com/api/location/{location}'

url_request = Request(url)
url_request.add_header('Accept', '*/*')
with urllib.request.urlopen(url_request) as req:
    request_result = json.loads(req.read())
    print(f"Weather forecast for {request_result['title']}: \n")
    print()


    for key in request_result['consolidated_weather']:
        #print(key)
        for secondaryKey in key:
            print(secondaryKey)
