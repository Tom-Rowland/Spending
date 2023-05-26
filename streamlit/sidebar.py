import streamlit as st

def main(df):
    def modify_all_categories():
        for cat in cat_choices:
            st.session_state[cat] = st.session_state.sel
        return

    
    st.sidebar.checkbox('Select/Deselect all categories', key='sel', on_change=modify_all_categories,value=True)
    st.sidebar.header("Categories")
    categories =  list(df[['Category','Amount']].groupby('Category').sum().sort_values(by=['Amount']).index)
    categories.remove('Income')

    cat_boxes = []
    for cat in categories:
        cat_boxes.append(st.sidebar.checkbox(cat,value=True, key=cat))

    cat_choices = {categories[i]:cat_boxes[i] for i in range(len(categories))}
    selected_categories = [cat for cat, selected in cat_choices.items() if selected]

    selected_df = df[(df['Category'].isin(selected_categories)) & (df['Category'] != 'Income')]
    selected_df.loc[:,'Amount'] = abs(selected_df['Amount'])

    cat_spend = str(int(selected_df['Amount'].sum()))

    return selected_df, cat_spend