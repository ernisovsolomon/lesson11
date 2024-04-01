'''
Анонимные функции / lambda
'''
'''
Задача 1
'''
cities = ['Москва', 'Bishkek', 'Алмата', 'Berlin', 'Ankara', 'Amsterdam']

def make_to_lower(city_name):
    return city_name.lower()

cities_lower = list(map(make_to_lower, cities))

print(cities_lower)