"""
@author: Mátyás

"""
import json
import pandas as pd

# Json with country, latitude, longitude.
with open('country_coordinates.json', 'r',encoding= 'utf-8') as file:
    coordinates = json.load(file)

# Json with athlete information.
with open('info_of_athletes.json', 'r',encoding= 'utf-8') as file:
    athletes = json.load(file)

# Isolating the countries from the previous file.
country_list_from_athletes = []

# Adding all the countries to one list. It will be counted.
for athlete in athletes:
    country = athlete['country']
    country_list_from_athletes.append(country)
    

# Rename the two countries, that exist, but with a different name.

country_list_from_athletes = [item.replace("Czech Republic", "Czechia") for item in country_list_from_athletes]

country_list_from_athletes = [item.replace("Ivory Coast", "Côte d'Ivoire") for item in country_list_from_athletes]


countries_info_from_api = []
# Connecting the informations. 
for element in coordinates:
    try:
        case = country_list_from_athletes.count(element['country'])
        element["case"] = case
        countries_info_from_api.append(element)
    except:
        pass
        # I ignore the empty dictionaries here.
   
output = pd.DataFrame(countries_info_from_api)

output.to_csv("cases_in_countries.csv", index = False)

