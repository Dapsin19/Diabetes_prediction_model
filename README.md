# 🩺 Diabetes Prediction Model

This project uses **Automated Machine Learning (AutoML)** with **PyCaret** to develop a binary classification model that predicts whether a patient is diabetic or not using a dataset from kaggle https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database. The best-performing model was the **Random Forest Classifier**, selected based on accuracy, AUC, and interpretability.

---

## 📁 Project Structure


---

## 🚀 Features

- AutoML with PyCaret
- Feature preprocessing (imputation, encoding, scaling)
- Model comparison and tuning
- ROC, AUC, precision-recall analysis
- Deployment-ready `.pkl` model

---

## 📊 Dataset

This model was trained on a publicly available diabetes dataset. It includes features such as:

- Glucose level  
- BMI  
- Blood pressure  
- Age  
- Insulin  
- Skin thickness  
- Diabetes pedigree function  
- Outcome (0 = Non-diabetic, 1 = Diabetic)

---

## ⚙️ How to Use the Diabetes Prediction Model
o use the model for predictions in a Python script or Jupyter notebook:

Ensure that you have the required packages installed:

pycaret

pandas

Load the saved model using PyCaret’s load_model() function.

Prepare a DataFrame with patient data. The input must contain the same features that were used to train the model.

Use predict_model() to generate a prediction. The model will return a Label column where:

0 means the patient is not diabetic

1 means the patient is likely diabetic

# How to Run the Interactive Diabetes Prediction App with Streamlit
This project also includes a Streamlit-powered web app that allows users to interact with the model by entering patient health data through a simple user interface.

🛠️ Steps to Run the App
Create a Python file named app.py.

Paste the full app code inside app.py (you'll find it below).

Make sure your trained model file (diabetes_model.pkl) is in the same directory.

Run the app with the following command:

**bash**

_streamlit run app.py_

A browser window will automatically open with the app interface.

📋 What the App Does
The app collects the following inputs:

Glucose Level

Blood Pressure

Skin Thickness

Insulin

BMI (Body Mass Index)

Diabetes Pedigree Function

Age

Number of Pregnancies

When the "Predict" button is clicked, the model processes the input and returns whether the patient is likely diabetic or not.

