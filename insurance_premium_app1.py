# insurance_premium_app.py

import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Insurance Premium Estimator")
st.write("Estimate your annual insurance premium based on your health profile.")

# User input fields
age = st.slider("Age", 18, 100, 30)
bmi = st.number_input("BMI (Body Mass Index)", 10.0, 50.0, 25.0)
history_cancer = st.selectbox("History of Cancer in Family", [0, 1])
chronic_disease = st.selectbox("Any Chronic Diseases", [0, 1])
diabetes = st.selectbox("Diabetes", [0, 1])
bp_problems = st.selectbox("Blood Pressure Problems", [0, 1])
transplant = st.selectbox("Any Transplants", [0, 1])
allergies = st.selectbox("Known Allergies", [0, 1])
surgeries = st.slider("Number of Major Surgeries", 0, 5, 0)

# Prepare input
input_df = pd.DataFrame({
    'Age': [age],
    'BMI': [bmi],
    'HistoryOfCancerInFamily': [history_cancer],
    'AnyChronicDiseases': [chronic_disease],
    'Diabetes': [diabetes],
    'BloodPressureProblems': [bp_problems],
    'AnyTransplants': [transplant],
    'KnownAllergies': [allergies],
    'NumberOfMajorSurgeries': [surgeries]
})

input_df['Age_BMI'] = input_df['Age'] * input_df['BMI']
input_df['Chronic_Diabetes'] = input_df['AnyChronicDiseases'] * input_df['Diabetes']
input_df['BMI_Surgeries'] = input_df['BMI'] * input_df['NumberOfMajorSurgeries']

# Predict button
if st.button("Estimate Premium"):
    premium = model.predict(input_df)[0]
    st.success(f"Estimated Annual Insurance Premium: ₹{premium:,.2f}")