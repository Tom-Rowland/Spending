import pandas as pd
import json

with open ('mapping.json', 'r') as file:
    data = file.read()
    mapping = json.loads(data)

def standard_mapping(description, mapping=mapping):
    for category in mapping.keys():
        for keyword, subcategory in mapping[category].items():
            if keyword in description:
                return category, subcategory
    return None, None
    
def office_canteen(description, amount):
    if 'ZETTLE_*ELIOR' in description:
        category = 'Food in office'
        subcategory = 'Breakfast' if abs(amount) <= 2.50 else 'Lunch'
        return category, subcategory
