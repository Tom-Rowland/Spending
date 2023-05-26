import streamlit as st
import pandas as pd

def main():
    uploaded_file = st.sidebar.file_uploader("Please upload a file", type=['csv'])
    if uploaded_file:
        df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    else:
        df = pd.DataFrame(columns=['Date','Category','Subcategory','Amount',])

    if df['Date'].dtype in ['str','object']:
        df['Date'] = pd.to_datetime(df['Date'],dayfirst=True)
    return df