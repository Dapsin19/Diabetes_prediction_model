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

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Dapsin19/Diabetes-prediction-model.git
cd diabetes-prediction-model
