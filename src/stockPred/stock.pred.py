import yfinance as yf
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import keras as ks
import sklearn as sk
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


