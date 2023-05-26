import streamlit as st

def main(df):
    income   = int(df[df['Category']=='Income']['Amount'].sum())
    expenses = int(abs(df[~df['Category'].isin(['Income', 'Savings'])]['Amount'].sum()))
    savings  = int(abs(df[df['Category']=='Savings']['Amount'].sum()))

    balance = income - expenses - savings
    if balance > 0:
        savings += balance

    for kpi in [income, expenses, savings]:
        kpi = '£' + str(kpi)

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader('Net income')
        st.subheader(income)

    with middle_column:
        st.subheader('Expenses')
        st.subheader(expenses)

    with right_column:
        st.subheader('Savings')
        st.subheader(savings)