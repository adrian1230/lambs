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

open_tick = []

for j in range(len(lit)):
    data = yf.Ticker(lit[j])
    df = data.history(period=hist[0],start=hist[1],end=hist[2])
    open_tick.append(df.Open)

length = 0

for f in range(len(open_tick)):
    length += len(open_tick[f])

open_tick = np.array(open_tick).reshape((int(length/len(lit)),len(lit)))

close_tick = []

for j in range(len(lit)):
    data = yf.Ticker(lit[j])
    df = data.history(period=hist[0],start=hist[1],end=hist[2])
    close_tick.append(df.Close)

close_tick = np.array(close_tick).reshape((int(length/len(lit)),len(lit)))

high_tick = []

for j in range(len(lit)):
    data = yf.Ticker(lit[j])
    df = data.history(period=hist[0],start=hist[1],end=hist[2])
    high_tick.append(df.High)

high_tick = np.array(high_tick).reshape((int(length/len(lit)),len(lit)))

low_tick = []

for j in range(len(lit)):
    data = yf.Ticker(lit[j])
    df = data.history(period=hist[0],start=hist[1],end=hist[2])
    low_tick.append(df.Low)

low_tick = np.array(low_tick).reshape((int(length/len(lit)),len(lit)))

volume_tick = []

for j in range(len(lit)):
    data = yf.Ticker(lit[j])
    df = data.history(period=hist[0],start=hist[1],end=hist[2])
    volume_tick.append(df.Volume)

volume_tick = np.array(volume_tick).reshape((int(length/len(lit)),len(lit)))

print(low_tick)

Closingchart = pd.DataFrame(
    close_tick,
    columns=[lit[d] for d in range(len(lit))]
)

Openchart = pd.DataFrame(
    open_tick,
    columns=[lit[d] for d in range(len(lit))]
)

Highchart = pd.DataFrame(
    high_tick,
    columns=[lit[d] for d in range(len(lit))]
)

Lowchart = pd.DataFrame(
    low_tick,
    columns=[lit[d] for d in range(len(lit))]
)

Volumechart = pd.DataFrame(
    volume_tick,
    columns=[lit[d] for d in range(len(lit))]
)

st.write("""
## Open Price
"""
)
st.line_chart(Openchart)

st.write("""
## High Price
"""
)
st.line_chart(Highchart)

st.write("""
## Low Price
"""
)
st.line_chart(Lowchart)

st.write("""
## Volume
"""
)
st.line_chart(Volumechart)

st.write("""
## Closing Price
"""
)
st.line_chart(Closingchart)


