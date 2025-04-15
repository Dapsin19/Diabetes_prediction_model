# Streamlit App Code (for reference)
import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the trained model
model = load_model("diabetes_model")

st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details below to predict diabetes status.")

# Collect user input
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=85)
bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=33.6)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.627)
age = st.number_input("Age", min_value=1, max_value=120, value=50)
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=2)

# Create input DataFrame
input_data = pd.DataFrame({
    "Glucose": [glucose],
    "BloodPressure": [blood_pressure],
    "SkinThickness": [skin_thickness],
    "Insulin": [insulin],
    "BMI": [bmi],
    "DiabetesPedigreeFunction": [dpf],
    "Age": [age],
    "Pregnancies": [pregnancies]
})

# Predict and display result
if st.button("Predict"):
    result = predict_model(model, data=input_data)
    prediction = int(result["Label"][0])
    if prediction == 1:
        st.error("⚠️ This patient is likely diabetic.")
    else:
        st.success("✅ This patient is likely not diabetic.")
