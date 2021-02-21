import streamlit as st
import json as js
import os
import datetime as dt

st.write("""
# Add new data to json and let sentinel figures its sentiment
""")

st.write("""
***
""")

st.text("Example:")

st.text("Martina laughed when her mother dropped a pie upside down on the floor.;;")

st.text("He was like a cock who thought the sun had risen to hear him crow.")

st.text("use ;; to separate sentences")

input = st.text_area("Add on some sentences","")

input = input.split(";;")

with st.echo():
    def get_punctuation():
        return '!!!'

for i in range(len(input)):
    if input[i] == "":
        del input[i]

for e in range(len(input)):
    input[e] = input[e].strip()

f = open("data.json", "a+")

for o in range(len(input)):
    queue = {"date": dt.datetime.today().strftime("%Y-%m-%d"),"text": input[o]}
    move = js.dumps(queue,indent=4)
    old = js.load(f)
    old.update(move)
    # f.write(move)
    # f.write(",")

f.close()

with st.beta_expander("Check your data in json format"):
    st.text("asd")