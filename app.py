import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Monthly Spending Tracker",
                   page_icon=":money_with_wings:",
                   layout="wide")

df = pd.read_excel('april.xlsx')

# SIDEBAR
st.sidebar.header("Settings")
categories = st.sidebar.multiselect(
    "Select categories to show",
    options=df[df['Category']!='Income']['Category'].unique(),
    default=df[df['Category']!='Income']['Category'].unique()
)

selected_df = df[(df['Category'].isin(categories)) & (df['Category'] != 'Income')]
selected_df['Amount'] = abs(selected_df['Amount'])


# MAINPAGE
st.title("Spending")
st.markdown('##')

# TOP KPIs
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


# MAIN PIE CHART
df_grouped = selected_df[['Category','Amount']].groupby('Category').sum()
print(df_grouped.index)

fig_labels = df_grouped.index
fig_values = df_grouped['Amount']

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