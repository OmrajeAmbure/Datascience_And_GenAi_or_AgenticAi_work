import streamlit as st
import pandas as pd
import numpy as np

# App Title and Descriptions 
st.title("My First Streamlit App",text_alignment="left")
st.write("This is a Simple app to demonstrate the basic functionalities of Streamlit")

# Interactive Widgets in the Sidebar 
st.sidebar.header("User Input Features ")

# Text Input
user_name = st.sidebar.text_input("What is Your name ? ","Omraje Ambure")

# Slider 
age = st.sidebar.slider("Select Your Age ",0,100,25)

# Selectbox
fevarote_color = st.sidebar.selectbox("What is your favorite color?",['Blue','Red','Green','Yellow'])

# Main Page Content
st.header(f"Welcome, *{user_name}*!")
st.write(f"You are **{age}** years old and your favorate color is **{fevarote_color}**")

# Displaying Data
st.subheader("Here's are some random data: ")

data = pd.DataFrame(
    np.random.randn(10,5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

if st.button("Say Hello"):
    st.write("Hello There!")
else:
    st.write("Goodbye")


