import streamlit as st
import plotly.graph_objects as go

def main(df):
    income_grouped = df[df['Category']=='Income'][['Subcategory','Amount']].groupby('Subcategory').sum()

    fig_labels = income_grouped.index
    fig_values = income_grouped['Amount']

    fig = go.Figure(data=[go.Pie(labels=fig_labels, values=fig_values)])
    fig.update_traces(
        textinfo='label+value+percent',
        texttemplate='%{label}: £%{value:.0f}, %{percent}'
    )
    # Apply CSS styling to center the pie chart
    fig.update_layout(
        autosize=True,
        width=400,
        height=400,
        margin=dict(l=50, r=50, b=50, t=50),
        paper_bgcolor='rgba(0,0,0,0)',
    )

    # Display the chart using Streamlit
    st.plotly_chart(fig, use_container_width=True)