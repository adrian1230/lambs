import yfinance as yf
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

st.write("""
# Compare Stocks from Yahoo Finance

feature **Closing price** and **Volume**
""")

st.header("Enter up to 5 stock codes!")

st.subheader("Example Input: Nasdaq, AAPL, FTSE 100")

stock_codes = "AAPL, Gold "

lit = st.text_area("Stock Input", stock_codes)

lit = lit.split(',')

for i in range(len(lit)):
    lit[i] = lit[i].strip()

null = []

for k in range(len(lit)):
    if lit[k] == "":
        null.append(k)

for i in range(len(null)):
    del lit[null[i]]

if len(lit) > 5:
    raise ValueError("More than 5")

if len(lit) < 2:
    raise ValueError("Cannot compare")

print("These are your selected stocks:")

for p, q in enumerate(lit):
    print(p, '=>', q)

st.write("""
***
""")

st.header("Your selected stocks")
lit

