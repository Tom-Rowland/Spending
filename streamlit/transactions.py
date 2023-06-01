import streamlit as st
import category_spend

def main(selected_df, cat_spend):
    sort_order = ['Date','Category','Subcategory','Amount']
    for col in sort_order:
        if col not in selected_df.columns:
            sort_order.remove(col)
    st.dataframe(selected_df.sort_values(['Date','Category','Subcategory','Amount']))

    category_spend.main(cat_spend)