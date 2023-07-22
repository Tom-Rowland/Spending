import pandas as pd
import json

with open('mapping.json', 'r') as file:
    data = file.read()
    mapping = json.loads(data)

def mapping(description, mapping=mapping):
    for category in mapping.keys():
        for keyword, subcategory in mapping[category].items():
            if keyword in description:
                return category, subcategory
    return None, None