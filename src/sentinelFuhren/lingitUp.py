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
        pos -> ner
        coreConcepts -> extra
        ner -> coreConcepts
        Org -> ner
        Fin -> ner
        Dated -> ner
        Loc -> ner
        Date -> ner
        BBegin -> tags
        EEnd -> tags
        SSingle -> tags
        OOther -> tags
        tags -> Org
        OOther -> extra
        tags -> Fin 
        tags -> Dated
        tags -> Loc
        tags -> Date
        IIntermediate -> tags
        ner -> trainingData
        trainingData -> training
    }
''')

with st.beta_expander("Check your data"):
    st.text("asd")