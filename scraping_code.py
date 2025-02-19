#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modified: 30/12/2024

@author: Everyone
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import time
import json
import os
    
# =============================================================================
# 1.Data Gathering and Data Storage for Pages A-Z.
# =============================================================================

# Specify the path for the directory.
path = './pagesAZ'

# Create a folder.
os.mkdir(path)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

url = 'https://en.wikipedia.org/wiki/List_of_doping_cases_in_sport_(A)'
request1 = Request(url)
response = urlopen(request1)

    
for page in letters: 
    time.sleep(2)
    url = 'https://en.wikipedia.org/wiki/List_of_doping_cases_in_sport_' + "(" + page + ")"
    

    request1 = Request(url)
    page_num = urlopen(request1).read().decode("utf-8") 

    with open ("pagesAZ/" + page +  "_page.html", "w", encoding="utf-8") as f:
       f.write(page_num)
    print(f"Page {page} created.")


# =============================================================================
# 2. Data Gathering and DataStorage for athletes
# =============================================================================


info_of_athletes = []
text_to_check  = "(page does not exist)"
for page in letters:

    doc = open (f"pagesAZ/{page}_page.html", "r", encoding="utf8")
    soup = BeautifulSoup(doc, "html.parser")
    tbody_element = soup.find("tbody")
    table_rows = tbody_element.find_all("tr")

    
    if page == "A": # The first page indexed different.
    
        for row in table_rows [1:]: 
            athlete = {}
            athlete["name"] = row.find("td").text.strip()
            athlete["country"] = row.find_all("td")[1].text.strip()
            athlete["sport"] = row.find_all("td")[2].text.strip()
            athlete["substance"] = row.find_all("td")[4].text.split()
            try:
                title = row.td.find("a")["title"]
                if text_to_check in title: # For athletes with a link without a page. (Their name is red in the site.)
                    athlete["link"] = "Page does not exist."
                    athlete["birthday"] = "N/A"
             
                else:  # For athletes with a working link. (Their name is blue.)
                    athlete["link"] = row.td.find("a")["href"]
                    try: # For athletes with birthday info in the infobox.
                        time.sleep(0.2)    
                        url = 'https://en.wikipedia.org'+ athlete["link"]
                        html = urlopen(url).read().decode("utf-8")
                        soup = BeautifulSoup(html, "html.parser")
                        dob_element = soup.find(class_="bday")
                        athlete["birthday"] = dob_element.text.strip()
                        
                    except:
                        athlete["birthday"] = "N/A"
           
            except: # For athletes without a link. (Their name is black.)
                athlete["link"] = "Page does not exist."
                athlete["birthday"] = "N/A"
         
                
            
          
            info_of_athletes.append(athlete)
            
        print("We finished page A.") # Checking progress.
        
    else:# The rest of the pages follow the same indexing.
      
        for row in table_rows [1:]: 
            athlete = {}
            athlete["name"] = row.find("td").text.strip()
            athlete["country"] = row.find_all("td")[1].text.strip()
            athlete["sport"] = row.find_all("td")[2].text.strip()
            athlete["substance"] = row.find_all("td")[3].text.split()
            try:
                title = row.td.find("a")["title"]
                if text_to_check in title:
                    athlete["link"] = "Page does not exist."
                    athlete["birthday"] = "N/A"
                
                else:
                    athlete["link"] = row.td.find("a")["href"]
                    try:
                        time.sleep(0.2) 
                        url = 'https://en.wikipedia.org'+ athlete["link"]
                        html = urlopen(url).read().decode("utf-8")
                        soup = BeautifulSoup(html, "html.parser")
                        dob_element = soup.find(class_="bday")
                        athlete["birthday"] = dob_element.text.strip()      
               
                    except:
                        athlete["birthday"] = "N/A"
              
            except:
                athlete["link"] = "Page does not exist."
                athlete["birthday"] = "N/A"
             
            
            
            info_of_athletes.append(athlete)
             
        print(f"We finished page {page}.") # Checking progress.



df = pd.DataFrame(info_of_athletes, columns=[ "name", "country", "sport", "substance", "link","birthday"])
df.to_csv("group_9_athletes_information.csv", index=False)

with open("info_of_athletes.json", "w", encoding= "utf-8") as f:
    json.dump(info_of_athletes, f, indent=4, ensure_ascii=False)


    
    
