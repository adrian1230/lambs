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

input = input.split(";;")

for i in range(len(input)):
    if input[i] == "":
        del input[i]

with st.beta_expander("Check your data in json format"):
    st.text("asd")