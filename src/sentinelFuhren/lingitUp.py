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
        words -> pos
        words -> ner
        words -> extra

    }
''')

with st.beta_expander("Check your data"):
    st.text("asd")