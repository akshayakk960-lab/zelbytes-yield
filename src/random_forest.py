import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import (
    TimeSeriesSplit,
    cross_val_score
)

# ==========================
# Load Train/Test Data
# ==========================

X_train = pd.read_parquet(
    "data/processed/X_train.parquet"
)

X_test = pd.read_parquet(
    "data/processed/X_test.parquet"
)

y_train = pd.read_parquet(
    "data/processed/y_train.parquet"
)

y_test = pd.read_parquet(
    "data/processed/y_test.parquet"
)

# Convert target to Series
y_train = y_train.squeeze()
y_test = y_test.squeeze()

# ==========================
# Handle Missing Values
# ==========================

print("Missing values before cleaning")
print("X_train:", X_train.isna().sum().sum())
print("X_test :", X_test.isna().sum().sum())

# Fill NaN values using training medians
numeric_cols = X_train.select_dtypes(include=np.number).columns

X_train[numeric_cols] = X_train[numeric_cols].fillna(
    X_train[numeric_cols].median()
)

X_test[numeric_cols] = X_test[numeric_cols].fillna(
    X_train[numeric_cols].median()
)

print("\nMissing values after cleaning")
print("X_train:", X_train.isna().sum().sum())
print("X_test :", X_test.isna().sum().sum())

print("\nData Loaded Successfully")

# ==========================
# Linear Regression
# ==========================

lr = LinearRegression()

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

lr_mae = mean_absolute_error(
    y_test,
    lr_pred
)

lr_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        lr_pred
    )
)

lr_r2 = r2_score(
    y_test,
    lr_pred
)

# ==========================
# Random Forest
# ==========================

rf = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_mae = mean_absolute_error(
    y_test,
    rf_pred
)

rf_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        rf_pred
    )
)

rf_r2 = r2_score(
    y_test,
    rf_pred
)

# ==========================
# Model Comparison
# ==========================

print("\nMODEL COMPARISON")
print("---------------------------")

print("\nLinear Regression")
print("MAE :", round(lr_mae, 4))
print("RMSE:", round(lr_rmse, 4))
print("R2  :", round(lr_r2, 4))

print("\nRandom Forest")
print("MAE :", round(rf_mae, 4))
print("RMSE:", round(rf_rmse, 4))
print("R2  :", round(rf_r2, 4))

# ==========================
# Overfitting Check
# ==========================

rf_train_pred = rf.predict(X_train)

train_rmse = np.sqrt(
    mean_squared_error(
        y_train,
        rf_train_pred
    )
)

test_rmse = np.sqrt(
    mean_squared_error(
        y_test,
        rf_pred
    )
)

print("\nOVERFITTING CHECK")
print("---------------------------")
print("Train RMSE:", round(train_rmse, 4))
print("Test RMSE :", round(test_rmse, 4))

# ==========================
# TimeSeries Cross Validation
# ==========================

tscv = TimeSeriesSplit(
    n_splits=5
)

lr_cv = cross_val_score(
    lr,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

rf_cv = cross_val_score(
    rf,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

lr_cv = -lr_cv
rf_cv = -rf_cv

print("\nLINEAR REGRESSION CV MAE")
print(lr_cv)
print("Mean:", round(lr_cv.mean(), 4))
print("Std :", round(lr_cv.std(), 4))

print("\nRANDOM FOREST CV MAE")
print(rf_cv)
print("Mean:", round(rf_cv.mean(), 4))
print("Std :", round(rf_cv.std(), 4))

# ==========================
# Feature Importance
# ==========================

importance = rf.feature_importances_

imp_df = pd.DataFrame({
    "Feature": X_train.columns,
    "Importance": importance
})

imp_df = imp_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE")
print(imp_df)

plt.figure(figsize=(8, 5))

plt.bar(
    imp_df["Feature"],
    imp_df["Importance"]
)

plt.title(
    "Random Forest Feature Importance"
)

plt.xlabel("Features")
plt.ylabel("Importance")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/rf_feature_importance.png"
)

plt.close()

print(
    "\nFeature Importance Plot Saved:"
)
print(
    "reports/rf_feature_importance.png"
)

# ==========================
# Save Model
# ==========================

joblib.dump(
    rf,
    "models/random_forest_model.pkl"
)

print(
    "\nModel Saved:"
)
print(
    "models/random_forest_model.pkl"
)