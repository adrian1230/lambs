import streamlit as st
import os
import datetime as dt
import csv

st.write("""
# Let sentinel figures its sentiment
""")

st.write("""
***
""")

with st.echo():
    pseudocode = ''

st.graphviz_chart('''
    digraph {
        Sequential -> LSTM
        sentence -> words
        words -> coreConcepts
        coreConcepts -> pos
        coreConcepts -> ner
        coreConcepts -> extra
        ner -> coreConcepts
        ner -> weightMore
        pos -> weightLess
        weightMore -> trainingData
        weightLess -> trainingData
    }
''')

with st.beta_expander("Check your data"):
    st.text("asd")