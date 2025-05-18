# 📈 STAT-X: Short-term Atmospheric Temperature Forecasting using Machine Learning Models with Explainable-AI

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" height="100"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-learn" height="100"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg" alt="TensorFlow" height="100"/>

This repository contains the source code and dataset used in the research project **STAT-X**, which explores machine learning-based approaches to forecast **minimum and maximum daily temperatures** for the upcoming three days in **Kolkata, India**.

---

## Overview

**STAT-X** investigates the application of **supervised machine learning algorithms** to short-term temperature forecasting using historical weather data from **1973 to 2024**. The project focuses on **interpretable and accurate** predictions by integrating **Explainable AI (XAI)** tools.

---

## Dataset

* **Location**: Kolkata, India
* **Time Range**: 1973–2024
* **Features**: 13 weather-related attributes, including:
* **Target**: Predict Minimum and Maximum temperatures for the next 3 days

---

## Methodology

* **Algorithms Used**:

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor
  * Bagging Regressor
  * Gradient Boosting Regressor
  * Multi-Layer Perceptron

* **Evaluation Metrics**:

  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
  * Mean Absolute Percentage Error (MAPE)
  * Coefficient of Determination (R² Score)


---

## 🧠 Explainability

* **SHAP (SHapley Additive exPlanations)** – for global and local feature importance
* **LIME (Local Interpretable Model-agnostic Explanations)** – for instance-level explanations

---

## 📁 Contents

* Jupyter Notebook code files in `\code\`
* Data in `\data\`

---

For questions or more details, feel free to reach out. Citation details will be added upon publication.

---
