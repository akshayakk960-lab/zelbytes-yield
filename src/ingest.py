import pandas as pd
import os

# Define file paths safely
input_path = "data/raw/polyhouse_sensors.csv"
output_dir = "data/interim"
output_path = os.path.join(output_dir, "01_loaded.csv")

print("--- Starting Data Ingestion Script ---")

# Load CSV safely
if os.path.exists(input_path):
    df = pd.read_csv(input_path, parse_dates=["timestamp"])
else:
    print(f"Error: File not found at {input_path}")
    exit()

# Print metrics to terminal
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nFirst Rows:")
print(df.head())

# Create interim folder and save snapshot
os.makedirs(output_dir, exist_ok=True)
df.to_csv(output_path, index=False)
print("\nSnapshot saved successfully to data/interim/01_loaded.csv!")