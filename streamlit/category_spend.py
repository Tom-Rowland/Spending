import streamlit as st

def main(cat_spend):
    st.markdown(f"<h2 style='text-align: center; color: black;'>£{cat_spend}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: black;'>Spent across selected categories</p>", unsafe_allow_html=True)