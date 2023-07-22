import pandas as pd
import mapping

if __name__ == '__main__':
    statement = pd.read_csv('data/1 raw/StarlingStatement.csv', encoding='latin-1')
    statement.rename(columns={'Amount (GBP)': 'Amount', 'Reference':'Description'}, inplace=True)
    statement['Amount'] = statement['Amount'].astype(float)/2
    statement['Category'], statement['Subcategory'] = None, None

    for index, transaction in statement.iterrows():
        #Standard mapping
        category, subcategory = mapping.mapping(transaction['Description'])
        statement.at[index, 'Category'] = category
        statement.at[index, 'Subcategory'] = subcategory

    # Label groceries as 'Joint'
    statement.loc[statement['Category'] == 'Groceries', 'Subcategory'] = 'Joint'

    # Don't include top up as income
    topup_mask = statement['Description'].str.contains('top up|Topup', case=False)
    statement = statement.loc[~topup_mask]

    #Car fuel (labelled explicitly, description not useful)
    fuel_mask = statement['Spending Category'] == 'FUEL'
    statement.loc[fuel_mask, 'Category'] = 'Transport'
    statement.loc[fuel_mask, 'Subcategory'] = 'Car fuel'
    
    statement.to_csv('data/2 autoprocessed/AutoProcessedStarling.csv')
    statement.to_csv('data/3 manual changes/Starling.csv')