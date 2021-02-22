import streamlit as st
import json as js
import os
import datetime as dt

st.write("""
# Let sentinel figures its sentiment
""")

st.write("""
***
""")

with st.echo():
    def get_punctuation():
        return '!!!'

with st.beta_expander("Check your data in json format"):
    st.text("asd")