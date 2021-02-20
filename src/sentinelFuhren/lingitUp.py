import streamlit as st

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

input.split(";;")[0]

st.write("""
***
""")

st.text("Click the button to read the data as json")

btn = st.button("browse")

st.text(btn)