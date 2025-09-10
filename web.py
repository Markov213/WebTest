import streamlit as st

st.title("Hello, Streamlit! S1")
st.write("this is simple streamlit web app")

name = st.text_input("Enter your name", "Type here ...")
age = st.slider("Enter your age", 0, 120, 25)

if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")


df = {
    'Name': ['AHmed', 'Amir', 'Ali'],
    'Age': [35, 30, 22],}

st.dataframe(df)