data_from_api = [
    {'city': 'Kraków', 'province_id': 8, 'current_temp': 3.5},
    {'city': 'Warszawa', 'province_id': 1, 'current_temp': 2.8},
    {'city': 'Suwałki', 'province_id': 9, 'current_temp': -0.5},
    {'city': 'Gdańsk', 'province_id': 3, 'current_temp': -0.1},
    {'city': 'Rzeszów', 'province_id': 7, 'current_temp': 3.9},
    {'city': 'Wrocław', 'province_id': 2, 'current_temp': 5.0},
]

#cities = list(filter(lambda city: city ('current_temp') >= 0, data_from_api)

cities = [city for city in data_from_api if city['current_temp'] >= 0]

print(cities)