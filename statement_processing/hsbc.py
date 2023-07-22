import pandas as pd
import mapping

if __name__ == '__main__':
    statement = pd.read_csv('data/1 raw/TransactionHistory.csv',header=None)
    statement.columns = ['Date', 'Description','Amount']
    statement['Amount'] = statement['Amount'].str.replace(',', '').astype(float)
    statement['Description'] = statement['Description'].apply(lambda x: x.replace(" )))",""))
    statement['Category'], statement['Subcategory'] = None, None

    for index, transaction in statement.iterrows():
        #Standard mapping
        category, subcategory = mapping.mapping(transaction['Description'])
        statement.at[index, 'Category'] = category
        statement.at[index, 'Subcategory'] = subcategory
    
    # For food at office, determine if breakfast/lunch
    food_in_office_empty_subcategory = (statement['Category'] == 'Food in office') & (statement['Subcategory'] == '')
    statement.loc[food_in_office_empty_subcategory & (abs(statement['Amount']) < 2.50), 'Subcategory'] = 'Breakfast'
    statement.loc[food_in_office_empty_subcategory & (abs(statement['Amount']) >= 2.50), 'Subcategory'] = 'Lunch'
    
    # Label groceries from HSBC as 'Solo'
    statement.loc[statement['Category'] == 'Groceries', 'Subcategory'] = 'Solo'

    # Ignore transfers to starling accounts, not real expenditure
    statement = statement.loc[~statement['Description'].isin(['Thomas Rowland Cycle BP', 'MeganTom Joint Topup BP'])]
    statement.to_csv('data/2 autoprocessed/AutoProcessedTransactionHistory.csv')
    statement.to_csv('data/3 manual changes/HSBC.csv')