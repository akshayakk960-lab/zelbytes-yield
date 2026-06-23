# Monitoring Plan

## Model Artifact Handling

The trained Random Forest model is stored in the `models/` directory as `random_forest_model.pkl`. The Streamlit application loads this model at runtime to generate yield predictions.

## Prediction Logging

Each prediction should record the following information:

| Timestamp (UTC)      | Temperature (°C) | Humidity (%) | CO₂ (ppm) | Predicted Yield (kg) |
| -------------------- | ---------------- | ------------ | --------- | -------------------- |
| 2026-06-23T10:15:30Z | 22.0             | 88.0         | 900       | 4.59                 |

These logs can be stored in `logs/predictions.csv` for monitoring model usage and prediction trends.

## Retraining Triggers

The model should be retrained when:

* Prediction accuracy decreases noticeably.
* New sensor data becomes available.
* Environmental conditions change significantly.
* A new mushroom growing season begins.
* Monthly or quarterly model performance reviews indicate performance drift.

## Future Improvements

* Automate prediction logging.
* Monitor prediction drift over time.
* Retrain the model using newly collected sensor data.
* Deploy automated retraining using a scheduled pipeline.
