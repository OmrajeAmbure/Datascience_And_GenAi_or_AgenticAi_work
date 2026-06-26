import streamlit as st
import pandas as pd
st.title("My First Streamlit App Created by Omraje Ambure",text_alignment='justify')
st.write("Wlecome! This App Calculates The Square of a Number.")
# st.write(
#     pd.DataFrame(
#          {
#              "first column": [1, 2, 3, 4],
#              "second column": [10, 20, 30, 40],
#          }
#      )
# )
st.header("Select a Number")
number = st.slider("Pick The Number ",0,100,25,) # min,max,default

st.subheader("Result")
squared_number = number * number
st.write(f"The Square of **{number}** is **{squared_number}**.")
