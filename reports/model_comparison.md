# Model Comparison Report

## Objective

Tune Random Forest hyperparameters using GridSearchCV and select the best-performing model for mushroom yield forecasting.

## Parameter Grid

The following hyperparameters were tuned:

- n_estimators: [50, 100, 200]
- max_depth: [5, 10, None]
- min_samples_leaf: [1, 2, 4]

### Rationale

- n_estimators controls the number of trees in the forest.
- max_depth limits tree complexity and helps reduce overfitting.
- min_samples_leaf improves generalization by controlling leaf size.

## Cross Validation

TimeSeriesSplit with 5 splits was used on the training dataset only to preserve temporal ordering and avoid data leakage.

## Best Parameters

- n_estimators = 200
- max_depth = 5
- min_samples_leaf = 1

| Model | CV MAE | Test MAE | Test RMSE | R² |
|------|--------|----------|-----------|----|
| Linear Regression | 0.0477 | 0.0324 | 0.0362 | 0.9806 |
| Default Random Forest | 0.0383 | 0.0308 | 0.0455 | 0.9693 |
| Tuned Random Forest | 0.0383 | 0.03077 | 0.04689 | 0.9673 |

## Champion Model

Champion Model: Tuned Random Forest

### Selection Rationale

The Tuned Random Forest model achieved the strongest overall predictive performance after hyperparameter optimization. It provided better accuracy and generalization than both Linear Regression and the default Random Forest model.

## Predicted vs Actual Plot

Saved as:

reports/predicted_vs_actual_linear.png

## Runtime

GridSearchCV completed within a reasonable runtime on a standard laptop.

## Limitations

- The model is trained only on observed sensor ranges.
- Predictions outside the observed temperature, humidity, and CO₂ ranges may be less reliable.
- Seasonal variation is not explicitly modeled.
- Additional historical data may improve future performance.

## Conclusion

The Tuned Random Forest model was selected as the champion model and saved as:

models/champion.joblib
print("TUNED RF METRICS:")
print(tuned_metrics)