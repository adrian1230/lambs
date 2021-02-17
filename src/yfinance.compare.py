import yfinance as yf
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
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

feature **Closing price** and **Volume**
""")

st.header("Enter up to 5 stock codes!")

st.subheader("Example Input: AAPL, FTSE 100; 1d, 2010-03-14, 2015-03-14")

stock_codes = "AAPL, Gold, TSLA, MSFT, GE; 1d, {}, {}".format(last,today)

lit = st.text_area("Stock & History Input", stock_codes)

hist  = lit.split(';')[1].split(',')

lit = lit.split(';')[0].split(',')

for k in range(len(hist)):
    hist[k] = hist[k].strip()

nan = []

for g in range(len(hist)):
    if hist[g] == "":
        nan.append(g)

for t in range(len(nan)):
    del hist[nan[t]]

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

close_tick = []

for j in range(len(lit)):
    data = yf.Ticker(lit[j])
    df = data.history(period=hist[0],start=hist[1],end=hist[2])
    close_tick.append(df.Close)

length = 0

for f in range(len(close_tick)):
    length += len(close_tick[f])

close_tick = np.array(close_tick).reshape((int(length/len(lit)),len(lit)))

Closingchart = pd.DataFrame(
    close_tick,
    columns=[lit[d] for d in range(len(lit))]
)

st.write("""
## Closing Price
"""
)
st.line_chart(Closingchart)


