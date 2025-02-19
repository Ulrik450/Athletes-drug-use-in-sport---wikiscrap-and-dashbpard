# -*- coding: utf-8 -*-
"""
@author: Mona and Mátyás

"""

import pandas as pd
import time
import json
from urllib.request import urlopen

# =============================================================================
# Making a list from the countries.
# =============================================================================

data = pd.read_json("info_of_athletes.json")

country_list  = data["country"].unique()

country_list_sorted  = sorted(country_list)

country_list_sorted.pop(54)

# =============================================================================
# Finding the coordinates.
# =============================================================================

apikey = "6744d573e0598028803168zqr152b43" # Personal api-key.

country_coordinates = [] 

for country in country_list_sorted:
    
    country = country.replace(" ", "+")
    
    result = {}
    
    try:
        time.sleep(1.1) # Maximum 1 request / second.
        url = f"https://geocode.maps.co/search?country={country}&api_key={apikey}"   
        page = urlopen(url)
        content = page.read().decode("utf-8")
        country_info = json.loads(content)
        
        for info in country_info:         
            result["country"] = country_info[0]["display_name"]
            result["latitude"] = country_info[0]["lat"]
            result["longitude"] = country_info[0]["lon"]
                
    except: 
        pass
        # This statement creates empty dictionaries. I could not make it nicer.
        
    country_coordinates.append(result)

# =============================================================================
# Making a json output file.
# =============================================================================

with open('country_coordinates.json', 'w', encoding='utf-8') as f:
    json.dump(country_coordinates, f, ensure_ascii=False, indent=4)