import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import category_spend

def main(df, selected_df, cat_spend):
    st.checkbox('Show Combined Total?', key='show_total', value=True)
    if len(selected_df) > 0:
        if 'Subcategory' in selected_df.columns and len(set(selected_df['Category']))==1:
            cat_or_subcat_string = 'Subcategory'
        else:
            cat_or_subcat_string = 'Category'
        spending_timeline = pd.DataFrame(columns = selected_df[cat_or_subcat_string].unique(), index = pd.date_range(min(df['Date']),max(df['Date'])).date)
        spending_timeline.reset_index(inplace=True)
        spending_timeline.rename(columns={'index':'Date'},inplace=True)

        transactions= selected_df.copy(deep=True)
        for i, row in spending_timeline.iterrows():
            categories = list(row.index)
            categories.remove('Date')
            for category in categories:
                spending_timeline.loc[i,category] = transactions[(transactions[cat_or_subcat_string]==category) & (transactions['Date']<=row['Date'])]['Amount'].sum()
        if st.session_state['show_total']:
            spending_timeline['Total'] = spending_timeline.iloc[:,1:].sum(axis=1)

        cols = list(spending_timeline.columns)
        cols.remove('Date')
        
        fig = go.Figure()

        # Add line traces for each column
        for col in cols:
            fig.add_trace(go.Scatter(x=spending_timeline['Date'], y=spending_timeline[col], mode='lines', name=col))

        # Update layout
        fig.update_layout(
            title='Cumulative Spend',
            xaxis_title='Date',
            yaxis_title='£'
        )

        fig.update_xaxes(range=[df['Date'].min(), df['Date'].max()])
        fig.update_yaxes(range=[0, spending_timeline.iloc[-1,1:]])

        st.plotly_chart(fig, use_container_width=True)

        category_spend.main(cat_spend)