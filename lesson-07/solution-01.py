# Defining the dictionary of the Counties and cities
list_of_counntries_and_cities = {
    "Republic of Belarus": "Minsk",
    "Ukraine": "Kiev",
    "Poland": "Warshaw"
}

dict_from_country_to_city = {
    value: key
    for key, value in list_of_counntries_and_cities.items()
}

# Find the city name
def from_country_to_city(country):
    city = dict_from_country_to_city[country]
    return city

# Find the country name
def from_city_to_country(city):
    country = dict_from_country_to_city[city]
    return country