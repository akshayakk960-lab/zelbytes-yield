import pandas as pd
import joblib
import json

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

# Load training data
X_train = pd.read_parquet("data/processed/X_train.parquet")
y_train = pd.read_parquet("data/processed/y_train.parquet").squeeze()

# Parameter grid
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [5, 10, None],
    "min_samples_leaf": [1, 2, 4]
}

# Time-series cross-validation
tscv = TimeSeriesSplit(n_splits=5)

# GridSearchCV
grid_search = GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)

# Train
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Save champion model
joblib.dump(best_model, "models/champion.joblib")

# Save best parameters
with open("models/best_params.json", "w") as f:
    json.dump(grid_search.best_params_, f, indent=4)

print("Best Parameters:", grid_search.best_params_)
print("Champion model saved.")