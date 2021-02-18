import yfinance as yf
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import keras as ks
import sklearn as sk
import datetime as dt
import tensorflow as tf

tod = dt.date.today()

py1 = int(tod.strftime("%Y")) - 10

last = ""

last = tod.strftime("%{}-%m-%d").format(py1)

today = tod.strftime("%Y-%m-%d")

st.write("""
# Visualize and Predict One Stock from Yahoo Finance
""")

st.header("Enter the stock code here!")

st.subheader("Example Input: AAPL; 1d, 2010-03-14, 2015-03-14")

st.text("Train from 2010-03-14 to 2015-03-14")

stock_codes = "GE; 1d, {}, {}".format(last,today)

lit = st.text_input("Stock & History Input", stock_codes)

hist  = lit.split(';')[1].split(',')

lit = lit.split(';')[0].split(',')

for k in range(len(hist)):
    hist[k] = hist[k].strip()

for i in range(len(lit)):
    lit[i] = lit[i].strip()

if len(lit) > 1:
    raise ValueError("More than 1")

st.write("""
***
""")

st.header("Your selected stock: {}".format(lit[0]))

st.subheader("Training or Application")

choice = st.text_input("Training or Application; 0 vs 1: ", 1)

choice = int(choice)

if choice < 0 or choice > 1:
    raise ValueError("other than 1 or 0")

def option_(choice):
    if choice == 0:
        return "Training"
    elif choice == 1:
        return "Application"
    else:
        raise ValueError("Not an option")

st.subheader("You chose {}".format(option_(choice)))

data = yf.Ticker(lit[0])
df = data.history(start=hist[1],end=hist[2])
open_tick = []
open_tick.append(df.Open)
open_tick = np.array(open_tick).reshape(-1)
date_tick = []
date_tick.append(df.index)
date_tick = np.array(date_tick).reshape(-1)
for r in range(len(date_tick)):
    date_tick[r] = str(pd.to_datetime(str(date_tick[r]))).split(' ')[0]
close_tick = []
close_tick.append(df.Close)
close_tick = np.array(close_tick).reshape(-1)
high_tick = []
high_tick.append(df.High)
high_tick = np.array(high_tick).reshape(-1)
low_tick = []
low_tick.append(df.Low)
low_tick = np.array(low_tick).reshape(-1)
volume_tick = []
volume_tick.append(df.Volume)
volume_tick = np.array(volume_tick).reshape(-1)
dividends_tick = []
dividends_tick.append(df.Dividends)
dividends_tick = np.array(dividends_tick).reshape(-1)

Closingchart = pd.DataFrame(close_tick)

DateChart = pd.DataFrame(date_tick)

Openchart = pd.DataFrame(open_tick)

Highchart = pd.DataFrame(high_tick)

Lowchart = pd.DataFrame(low_tick)

Volumechart = pd.DataFrame(volume_tick,)

Dividendchart = pd.DataFrame(dividends_tick)

Chart = pd.concat([DateChart,Openchart,Highchart,Lowchart,Volumechart,Closingchart, Dividendchart],axis=1)

Chart.columns = ['Date','Open','High','Low','Volume','Dividends','Close']

Chart.to_csv('Now.csv')

if choice == 0:
    process = 0 
    while process != 1:
        st.header("Begin training now")
        st.text("Training ...")
        train = Chart.iloc[:round(len(Chart)*0.7),1:6]
        test = Chart.iloc[round(len(Chart)*0.7):,6]
        print(train.head())
        print(test.head())
        process += 1
    st.header("Training result")
        
        








