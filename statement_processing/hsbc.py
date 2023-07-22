import pandas as pd
import categorise

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

    statement.loc[statement['Category'] == 'Groceries', 'Subcategory'] = 'Solo'

statement.to_csv('data/2 autoprocessed/AutoProcessedTransactionHistory.csv')