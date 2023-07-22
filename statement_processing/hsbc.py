import pandas as pd
import categorise

if __name__ == '__main__':
    statement = pd.read_csv('data/1 raw/TransactionHistory.csv',header=None)
    statement.columns = ['Date', 'Description','Amount']
    statement['Description'] = statement['Description'].apply(lambda x: x.replace(" )))",""))
    statement['Category'], statement['Subcategory'] = None, None

    for index, transaction in statement.iterrows():
        #Standard mapping
        category, subcategory = categorise.standard_mapping(transaction['Description'])
        statement.at[index, 'Category'] = category
        statement.at[index, 'Subcategory'] = subcategory
    # For food at office, determine if breakfast/lunch

    # Label groceries from HSBC as 'Solo'
    statement.loc[statement['Category'] == 'Groceries', 'Subcategory'] = 'Solo'

    # Ignore transfers to starling accounts, not real expenditure
    statement = statement.loc[~statement['Description'].isin(['Thomas Rowland Cycle BP', 'MeganTom Joint Topup BP'])]
    statement.to_csv('data/2 autoprocessed/AutoProcessedTransactionHistory.csv')