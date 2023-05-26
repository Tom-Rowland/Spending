import streamlit as st
import pandas as pd

def main():
    uploaded_file = st.sidebar.file_uploader("Please upload a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, parse_dates=['Date'])
        return df
    else:
        return pd.DataFrame(columns=['Date','Category','Subcategory','Amount',])