import pandas as pd
import streamlit as st

def main(uploaded_df):
    min_date, max_date = uploaded_df['Date'].min(), uploaded_df['Date'].max()

    date_selection = st.sidebar.date_input(label = 'Select a timeframe to analyse',
                                value= (min_date,max_date),
                                min_value=min_date,
                                max_value=max_date)
    
    if date_selection and len(date_selection) ==2:
        df = uploaded_df[(date_selection[0] <= uploaded_df['Date']) & (uploaded_df['Date'] <= date_selection[1])]
    else:
        df = df = pd.DataFrame(columns=['Date','Category','Subcategory','Amount',])
    
    return df