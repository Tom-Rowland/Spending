import pandas as pd
import streamlit as st
import sidebar, top_KPIs, pie_chart, spend_timeline

st.set_page_config(page_title="Monthly Spending Tracker",
                   page_icon=":money_with_wings:",
                   layout="wide")

df = pd.read_csv('april.csv',parse_dates=['Date'])

# SIDEBAR
selected_df, cat_spend = sidebar.main(df)

# TOP KPIs
top_KPIs.main(df)

# MIN TABS
tab1, tab2, tab3 = st.tabs(["Pie Chart", "Spend Timeline" , "Transactions"])
with tab1:
# PIE CHART
    pie_chart.main(selected_df)
with tab2:
# SPEND TIMELINE
    spend_timeline.main(df, selected_df)
with tab3:
# INDIVIDUAL TRANSACTIONS
    st.dataframe(selected_df.sort_values(['Date','Category','Subcategory','Amount']))

st.markdown(f"<h2 style='text-align: center; color: black;'>£{cat_spend}</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: black;'>Spent across selected categories</p>", unsafe_allow_html=True)