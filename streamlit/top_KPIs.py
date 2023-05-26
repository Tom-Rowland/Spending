import streamlit as st

def main(df):
    income   = '£' + str(int(df[df['Category']=='Income']['Amount'].sum()))
    expenses = '£' + str(int(abs(df[~df['Category'].isin(['Income', 'Savings'])]['Amount'].sum()))  )
    savings  = '£' + str(int(abs(df[df['Category']=='Savings']['Amount'].sum())))

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