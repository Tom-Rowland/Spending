import pandas as pd
import datetime

def strings_in_description(strings,description):
    for string in strings:
        if string in description:
            return 1
    return 0

def transport(description):
    if strings_in_description(['TFL TRAVEL','TRAINLINE']):
        category = 'Transport'
        if 'TFL TRAVEL' in description:
            subcategory = 'TfL'
        if 'TRAINLINE' in description:
            subcategory = 'Train'
        return category, subcategory

def office_canteen(description, amount):
    if 'ZETTLE_*ELIOR' in description:
        category = 'Food in office'
        subcategory = 'Breakfast' if abs(amount) <= 2.50 else 'Lunch'
        return category, subcategory

def gift_cards(description):
    if 'CARDS GALORE' in description:
        category = 'Gifts'
        subcategory = 'Cards'
        return category, subcategory

def income(description, amount):
    if amount > 0:
        category = 'Income'
        subcategory = 'Pay' if 'KUBRICK' in description else 'Parents' if 'ROWLAND J&C' in description else None
        if subcategory:
            return category, subcategory

def cinema(description):
    if 'ODEON' in description:
        category = 'Entertainment'
        subcategory = 'Cinema'
        return category, subcategory

def groceries(description, source, date):
    if strings_in_description(['VILLAGE WHOLE FOOD', 'TESCO STORES', 'CO  OP GROUP','SAINSBURYS'],description):
        category = 'Groceries'
        subcategory = 'Joint' if source=='Starling' else 'Solo' if source=='HSBC' else None
        if '6545' in description and date.weekday() not in [5,6]:
            category = 'Food in office'
            subcategory = 'Lunch'
        return category, subcategory

def eating_out_takeaway(description):
    if ('BURGER KING' in description)\
    or ('DELIVEROO' in description):
        category = 'Eating Out/Takeaway'
        subcategory = 'Eating Out'
        return category, subcategory

def tv_subscriptions(description):
    if 'NOW X8818 Sports' in description:
        category = 'TV Subscription'
        subcategory = 'NowTV Sport'
        return category, subcategory

def drinks(description, date):
    if strings_in_description(['GLOBE   003700 LONDON'], description):
        category = 'Drinks'
        if 'GLOBE' in description and datetime.datetime.weekday() not in [5,6]:
            subcategory = 'Work drinks'
        return category, subcategory



