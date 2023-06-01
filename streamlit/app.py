import pandas as pd
import streamlit as st
import upload, date_selection, sidebar, top_KPIs, pie_chart, spend_timeline, category_spend, income_split

st.set_page_config(page_title="Monthly Spending Tracker",
                   page_icon=":money_with_wings:",
                   layout="wide")

# SIDEBAR
uploaded_df = upload.main()

if uploaded_df is not None:
    df = date_selection.main(uploaded_df)
    selected_df, cat_spend = sidebar.main(df)

    # TOP KPIs
    top_KPIs.main(df)

    # MIN TABS
    income_has_subcategories = 'Subcategory' in df.columns and len(df[df['Category']=='Income']['Subcategory'].unique()) > 0

    if income_has_subcategories:
        tab1, tab2, tab3, tab4 = st.tabs(["Pie Chart", "Spend Timeline" , "Transactions", "Income Split"])
    else:
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

    if income_has_subcategories:
        with tab4:
            income_split.main(df)


    # SPEND ACROSS SELECTED CATEGORIES
    category_spend.main(cat_spend)