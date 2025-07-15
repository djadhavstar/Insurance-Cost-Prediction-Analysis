# Insurance-Cost-Prediction-Analysis
End-to-end insurance premium prediction project combining data analysis in Tableau and machine learning in Python. Includes EDA, hypothesis testing, regression modeling, SHAP explainability, and a deployed Streamlit web app for real-time premium estimation.
tableau, data-visualization, machine-learning, healthcare, streamlit, shap, regression, python

Insurance Cost Prediction Project

📌 Project Overview

This is an end-to-end data science project focused on predicting annual health insurance premiums using demographic and medical history data. The project includes:

Exploratory Data Analysis and Hypothesis Testing in Python

Regression Modeling using Random Forest and XGBoost

Feature importance and model explainability with SHAP

Data visualization and insights via Tableau Public

Real-time premium estimation using a deployed Streamlit web app

🧠 Problem Statement

To build a model that estimates the insurance premium cost for a customer based on their health and demographic profile. 
This can be used by insurers to optimize pricing and by customers to get premium estimates in real time.

🎯 Target Metric

Primary: R² Score (Coefficient of Determination)

Supporting: Root Mean Squared Error (RMSE), Mean Absolute Error (MAE)

🔍 Project Steps

1. Exploratory Data Analysis (EDA)

Analyzed age, BMI, chronic illness, surgery count, and their correlation with insurance premium.
Identified high-risk factors and outliers visually using plots and Tableau dashboards.

2. Hypothesis Testing

Used t-tests and ANOVA to validate if conditions like diabetes, high blood pressure, or family cancer history significantly impact insurance costs.

3. Feature Engineering

Created features like AgeBMI, Chronic_Diabetes, and BMISurgeries to capture interactions.

4. Machine Learning Modeling

Models used:

Random Forest Regressor (Best R² ~0.755), Gradient Boosting Regressor, XGBoost Regressor, Linear Regression, Decission Tree, KNN

Cross-validation (KFold) used to ensure robustness.
SHAP values used to interpret model outputs and identify top influencing features.

5. Deployment with Streamlit

Built a Streamlit web application that takes user input and estimates insurance premium in real-time.

Model saved using pickle and loaded into the app.

6. Data Visualization with Tableau

Key EDA and insights visualized and shared via Tableau Public.

🧾 Final Model Performance

Best R² Score: 0.755 (Random Forest with GridSearch)

Top Predictive Features:

History of Cancer in Family
Age
Chronic Illness & Diabetes combination
Number of Major Surgeries

📊 Tableau Dashboard
https://public.tableau.com/app/profile/deodatt.jadhav/viz/Insurance_Cost_Prediction_Analysis/InsuranceCostPredictionAnalysis?publish=yes

🌐 Deployed App

🔗 Streamlit App (Real-time Premium Calculator) http://localhost:8501/

📁 Repository Structure

insurance-cost-prediction/
├── notebooks/
│   └─ insurance_cost_prediction.ipynb
├── app/
│   ├─ insurance_premium_app.py
│   └─ rf_model.pkl
├── requirements.txt
└── README.md

🧰 Tech Stack

Python, Pandas, NumPy, Scikit-learn, XGBoost
SHAP, Streamlit, Tableau
Jupyter Notebook, GitHub

[Read the Full Technical Walkthrough on Medium]
https://medium.com/@djadhavstar/predicting-health-insurance-premiums-with-machine-learning-an-end-to-end-project-0d2d0b24a0d0

📌 Author
Deodatt Jadhav
GitHub Profile

[Read the Full Technical Walkthrough on Medium](https://medium.com/p/dcd13c7d0302/edit))

📬 Contact
For any questions, please reach out via LinkedIn or open an issue in the repository.
https://www.linkedin.com/in/deodatt-jadhav-03b756ba/
