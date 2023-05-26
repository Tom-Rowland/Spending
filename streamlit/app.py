import pandas as pd
import streamlit as st
import upload, sidebar, top_KPIs, pie_chart, spend_timeline, category_spend

st.set_page_config(page_title="Monthly Spending Tracker",
                   page_icon=":money_with_wings:",
                   layout="wide")

# SIDEBAR
df = upload.main()
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
    sort_order = ['Date','Category','Subcategory','Amount']
    for col in sort_order:
        if col not in selected_df.columns:
            sort_order.remove(col)
    st.dataframe(selected_df.sort_values(['Date','Category','Subcategory','Amount']))

# SPEND ACROSS SELECTED CATEGORIES
category_spend.main(cat_spend)