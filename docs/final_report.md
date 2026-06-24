# Technical Report: Mushroom Yield Forecasting System

## 1. Problem Statement & Data Description
* **Context:** Why are we predicting mushroom yield? (Optimizing greenhouse environments, minimizing crop failure).
* **Target Variable:** Predicted Yield (kg).
* **Features:** Temperature (°C), Humidity (%), CO₂ (ppm).
* **Data Source:** Overview of the sensor dataset used.

## 2. Data Cleaning & Exploratory Data Analysis (EDA)
* **Cleaning:** How you handled missing values, outliers, or duplicate sensor readings.
* **EDA Highlights:** Mention key correlations (e.g., how high humidity or specific CO₂ levels correlate with larger mushroom growth).

## 3. Modeling Methodology & Evaluation Metrics
* **Algorithms Tried:** Random Forest Regressor (and any baseline models).
* **Feature Scaling:** Mention using the `MinMaxScaler`.
* **Temporal Split Rationale:** Explain why you split the data chronologically (e.g., training on early weeks, testing on later weeks) instead of a random split. *Rationale: Mushrooms grow over time; a random split would cause data leakage from the future into the past.*
* **Metrics:** Your final validation scores (MAE, RMSE, $R^2$).

## 4. Cloud Deployment & Production Monitoring
* **Deployment Architecture:** Streamlit web application hosted on Streamlit Community Cloud.
* **Monitoring Implementation:** Telemetry logging active at `logs/predictions.csv`.
* **Retraining Strategy:** Triggers based on data drift, metric decay, and seasonal mushroom growth shifts (copied straight from your Task 9 document).

## 5. Limitations & Future Work
* **Limitations:** Small dataset size, missing other critical variables (like soil moisture or light exposure).
* **Future Work:** Automated database logging (Supabase), real-time drift alerts, and automated retraining pipelines via Airflow or GitHub Actions.