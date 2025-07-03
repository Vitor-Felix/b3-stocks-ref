import streamlit as st

st.set_page_config(page_title="B3 Dashboard", layout="wide")

st.title("📊 B3 Stock & FII Dashboard")
ticker = st.text_input("Enter a ticker (e.g. PETR4, HGLG11):")

if ticker:
    st.info(f"You searched for: {ticker}")
    st.write("Here we’ll show data and charts soon.")
