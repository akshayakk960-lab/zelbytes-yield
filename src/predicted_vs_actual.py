import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Load data
X_test = pd.read_parquet("data/processed/X_test.parquet")
y_test = pd.read_parquet("data/processed/y_test.parquet").squeeze()

# Load model
model = joblib.load("models/champion.joblib")

# Predict
predictions = model.predict(X_test)

# Scatter plot
plt.figure(figsize=(8,6))
plt.scatter(y_test, predictions)

# Perfect-fit line (y = x)
min_val = min(y_test.min(), predictions.min())
max_val = max(y_test.max(), predictions.max())

plt.plot(
    [min_val, max_val],
    [min_val, max_val],
    '--'
)

plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual vs Predicted Yield")

plt.grid(True)
plt.tight_layout()

plt.savefig("reports/predicted_vs_actual_linear.png", dpi=300)
plt.close()

print("Linear graph saved.")