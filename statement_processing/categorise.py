import pandas as pd
import json

def standard_mapping(description):
    with open ('mapping.json', 'r') as file:
        mapping = file.read()
    
    for category in mapping.keys():
        for keyword, subcategory in mapping[category]:
            if keyword in description:
                return category, subcategory
    

def office_canteen(description, amount):
    if 'ZETTLE_*ELIOR' in description:
        category = 'Food in office'
        subcategory = 'Breakfast' if abs(amount) <= 2.50 else 'Lunch'
        return category, subcategory
