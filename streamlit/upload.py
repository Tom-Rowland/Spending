import streamlit as st
import pandas as pd

def main():
    uploaded_file = st.sidebar.file_uploader("Please upload a file", type=['csv', 'xlsx'])
    if uploaded_file:
        if uploaded_file.type =='text/csv':
            df = pd.read_csv(uploaded_file, parse_dates=['Date'])
        else:
            df = pd.read_excel(uploaded_file, parse_dates=['Date'])
    else: 
        df = pd.DataFrame(columns=['Date','Category','Subcategory','Amount',])

    return df