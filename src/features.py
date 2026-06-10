import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

df = pd.read_csv("data/raw/polyhouse_sensors.csv")

df["temp_humidity_interaction"] = (
    df["temperature_c"] * df["humidity_pct"]
)

X = df[
    [
        "temperature_c",
        "humidity_pct",
        "co2_ppm",
        "temp_humidity_interaction",
    ]
]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

X_scaled_df = pd.DataFrame(
    X_scaled,
    columns=X.columns
)

X_scaled_df.to_parquet(
    "data/processed/features.parquet",
    index=False
)

joblib.dump(
    scaler,
    "models/minmax_scaler.pkl"
)

print("Task 7 completed successfully!")
