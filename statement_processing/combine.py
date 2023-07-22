import pandas as pd

if __name__ == '__main__':
    personal = pd.read_csv('data/4 staging to combine/HSBC.csv')
    joint = pd.read_csv('data/4 staging to combine/Starling.csv')

    personal = personal.loc[:,['Date','Description','Amount','Category','Subcategory']]
    joint = joint.loc[:,['Date','Description','Amount','Category','Subcategory']]

    combined = pd.concat([personal,joint], ignore_index=True)
    combined['Date'] = pd.to_datetime(combined['Date'],dayfirst=True)
    combined.sort_values(by='Date')

    combined.to_csv('data/5 combined/combined.csv',index=False)