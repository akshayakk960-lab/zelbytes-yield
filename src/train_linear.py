import os
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Create folders if they don't exist
os.makedirs("models", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("reports/figures", exist_ok=True)

# Load train-test data
X_train = pd.read_parquet("data/processed/X_train.parquet")
X_test = pd.read_parquet("data/processed/X_test.parquet")
y_train = pd.read_parquet("data/processed/y_train.parquet").squeeze()
y_test = pd.read_parquet("data/processed/y_test.parquet").squeeze()
# Remove rows with missing values from training data
train_df = pd.concat([X_train, y_train], axis=1).dropna()

X_train = train_df[X_train.columns]
y_train = train_df[y_train.name]

# Remove rows with missing values from test data
test_df = pd.concat([X_test, y_test], axis=1).dropna()

X_test = test_df[X_test.columns]
y_test = test_df[y_test.name]

# Check feature names
print("Features:", list(X_train.columns))

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
pred_test = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, pred_test)
rmse = np.sqrt(mean_squared_error(y_test, pred_test))
r2 = r2_score(y_test, pred_test)

print(f"\nTest MAE:  {mae:.2f} kg")
print(f"Test RMSE: {rmse:.2f} kg")
print(f"Test R²:   {r2:.3f}")

# Coefficients
coef_df = pd.DataFrame({
    "Feature": X_train.columns,
    "Coefficient": model.coef_
})

print("\nFeature Coefficients")
print(coef_df)

# Save model
joblib.dump(model, "models/linear_regression.joblib")

# Save metrics
metrics = {
    "MAE": float(mae),
    "RMSE": float(rmse),
    "R2": float(r2)
}

with open("reports/metrics_linear.json", "w") as f:
    json.dump(metrics, f, indent=4)

# Save coefficients table
coef_df.to_csv(
    "reports/linear_coefficients.csv",
    index=False
)

# Residuals (actual - predicted)
residuals = y_test - pred_test

# Diagnostic plots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Residual vs Predicted
axes[0].scatter(pred_test, residuals, alpha=0.5)
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set_title("Residuals vs Predicted")
axes[0].set_xlabel("Predicted Yield (kg)")
axes[0].set_ylabel("Residual (kg)")

# Residual vs Humidity
axes[1].scatter(X_test["humidity_pct"], residuals, alpha=0.5)
axes[1].axhline(0, color="red", linestyle="--")
axes[1].set_title("Residuals vs Humidity")
axes[1].set_xlabel("Humidity")
axes[1].set_ylabel("Residual (kg)")

plt.tight_layout()
plt.savefig("reports/figures/residuals_linear.png", dpi=150)
plt.close()

print("\nFiles Saved:")
print("- models/linear_regression.joblib")
print("- reports/metrics_linear.json")
print("- reports/linear_coefficients.csv")
print("- reports/figures/residuals_linear.png")

print("\nTask 5 completed successfully.")