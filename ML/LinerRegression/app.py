import streamlit as slt
import pickle
import numpy as np


model = pickle.load(open(r'E:/AIandMl project/NIT Course/Python/ML/Liner_regression_model.pkl','rb'))

slt.title("Salary Predication App")

slt.write("This app predicts the salary based on years of experience using a simple liner regression model")

years_of_exp = slt.number_input("Enter the Years of Experience : ",min_value=0.0,max_value=50.0,value=2.0,step=0.1)

if slt.button("Predict Salary"):
    experience_input  = np.array([[years_of_exp]])
    predication = model.predict(experience_input)
    slt.success(f"The predicated salary for {years_of_exp} years of experience is: ${predication[0]:,.2f}")

slt.write("The model was trained using a dataset of salaries and years of experience. bulit model by preameter")