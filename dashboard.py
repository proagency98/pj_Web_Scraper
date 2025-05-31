import streamlit as st
import pandas as pd

st.title("Dashboard de Scraping")

df = pd.read_csv("data/books.csv", encoding='utf-8-sig')

st.dataframe(df)