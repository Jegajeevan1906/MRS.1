import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Public Google Sheet CSV link
sheet_url = "https://docs.google.com/spreadsheets/d/1HIEGFg0UEOGebNTPY2XURYChdajFXD-0iCEonwfNGdg/edit?usp=sharing"
df = pd.read_csv(sheet_url)

# Sort & show
df = df.sort_values(by="Sales", ascending=False)
st.write(df)

st.bar_chart(df.set_index("Employee")["Sales"])
