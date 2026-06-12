# Linear Regression Diagnostics

## Test Metrics

* MAE: 0.03 kg
* RMSE: 0.04 kg
* R²: 0.980

## Coefficient Interpretation

* Temperature (temperature_c) has the strongest positive impact on mushroom yield.
* Humidity (humidity_pct) shows a small positive relationship with yield.
* CO₂ concentration (co2_ppm) also contributes positively to yield.

## Residual Analysis

Residuals were calculated as:

actual yield - predicted yield

The residual plots indicate that prediction errors are small and centered around zero.

No strong pattern is visible in the residuals versus humidity plot, suggesting that the linear model captures most of the relationship between the variables and yield.

## Baseline Evaluation

The model achieved an R² score of 0.980, indicating that approximately 98% of the variability in mushroom yield is explained by the input features.

This is an excellent baseline performance for a Linear Regression model.

## Recommendation

Keep Linear Regression as the baseline model.

Future improvements may include:

* Additional feature engineering
* Lag and rolling-window features
* Random Forest Regression
* Gradient Boosting Regression
* XGBoost for nonlinear relationships
