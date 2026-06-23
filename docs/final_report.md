# Mushroom Yield Forecast – Final Report

## Executive Summary

This project predicts daily oyster mushroom yield using environmental sensor data such as temperature, humidity, and CO₂ concentration. A Tuned Random Forest Regressor was selected as the final model after comparing it with a Linear Regression baseline. The model was deployed using Streamlit and includes a monitoring plan for future improvements.

## 1. Problem Statement

The objective of this project is to predict mushroom yield accurately using environmental sensor data collected from a polyhouse. Accurate predictions help farmers improve production planning and resource management.

## 2. Dataset

The dataset contains environmental features including:

* Temperature (°C)
* Humidity (%)
* CO₂ (ppm)
* Daily mushroom yield (kg)

Missing values were handled using median imputation, and the data was split into training and testing datasets.

## 3. Exploratory Data Analysis

* Analyzed feature distributions.
* Generated scatter plots and correlation analysis.
* Identified relationships between environmental variables and yield.

## 4. Feature Engineering

* Selected important environmental features.
* Applied preprocessing and validation using TimeSeriesSplit cross-validation.

## 5. Models Evaluated

### Linear Regression

* Used as the baseline model.
* Evaluated using MAE, RMSE, and R².

### Random Forest Regressor

* Improved prediction performance.
* Hyperparameters optimized using GridSearchCV.
* Selected as the champion model.

## 6. Model Performance

Include your actual results here.

| Model               | MAE          | RMSE         | R²           |
| ------------------- | ------------ | ------------ | ------------ |
| Linear Regression   | (your value) | (your value) | (your value) |
| Tuned Random Forest | (your value) | (your value) | (your value) |

The Tuned Random Forest model achieved the best overall performance and was selected for deployment.

## 7. Streamlit Application

A Streamlit web application was developed to:

* Enter temperature, humidity, and CO₂ values.
* Predict daily mushroom yield.
* Display prediction results through an interactive interface.

Deployment URL:
(Add your Streamlit URL after deployment.)

## 8. Monitoring Plan

Prediction logs are stored with timestamps and sensor values. Model retraining should be performed when:

* New sensor data becomes available.
* Prediction accuracy decreases.
* Environmental conditions change significantly.
* Periodic performance reviews indicate model drift.

## 9. Limitations

* Limited historical data.
* Only three environmental features were used.
* Performance may decrease under unseen environmental conditions.

## 10. Future Work

* Collect larger datasets.
* Include additional sensor features.
* Automate model retraining.
* Improve deployment monitoring.
* Integrate real-time IoT sensor data.

## Conclusion

The project successfully developed and deployed a machine learning solution for mushroom yield prediction. The Tuned Random Forest model demonstrated superior performance and provides a practical decision-support tool for smart agriculture.
