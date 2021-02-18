import yfinance as yf
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import keras as ks
import scklearn as sck
import datetime as dt

tod = dt.date.today()

pm1 = int(tod.strftime("%m"))

last = ""

if pm1 == 1:
    pm1 = str(12)
    y = int(tod.strftime("%Y"))-1
    y = str(y)
    last = tod.strftime("{}-{}-%d").format(y,pm1)

if pm1 != 1:
    pm1 = pm1 - 1
    pm1 = str(pm1)
    last = tod.strftime("%Y-{}-%d").format(pm1)

today = tod.strftime("%Y-%m-%d")

st.write("""
# Compare Stocks from Yahoo Finance
""")

st.header("Enter stock codes here!")

st.subheader("Example Input: AAPL, FTSE 100; 1d, 2010-03-14, 2015-03-14")

stock_codes = "AAPL, Gold, TSLA, MSFT, GE; 1d, {}, {}".format(last,today)

lit = st.text_area("Stock & History Input", stock_codes)

hist  = lit.split(';')[1].split(',')

lit = lit.split(';')[0].split(',')

for k in range(len(hist)):
    hist[k] = hist[k].strip()

for i in range(len(lit)):
    lit[i] = lit[i].strip()

print("These are your selected stocks:")

for p, q in enumerate(lit):
    print(p, '=>', q)

st.write("""
***
""")

st.header("Your selected stocks")
lit



