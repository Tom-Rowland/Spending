import pandas as pd

df = pd.read_csv('data/raw/TransactionHistory.csv',header=None)
print(df.iloc[0])
df.columns = ['Date', 'Description','Amount']
print(df.iloc[0:5])
df['Description'] = df['Description'].apply(lambda x: x.replace(" )))",""))

print(df.iloc[0:5])