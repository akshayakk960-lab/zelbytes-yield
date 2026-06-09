import os
import pandas as pd

# Define paths safely
input_path = "data/raw/polyhouse_sensors.csv"
interim_dir = "data/interim"
processed_dir = "data/processed"

# Output target paths
csv_output_path = os.path.join(interim_dir, "01_loaded.csv")
parquet_output_path = os.path.join(processed_dir, "02_cleaned.parquet")

print("--- Starting Data Ingestion & Cleaning Pipeline ---")

if os.path.exists(input_path):
    # Load and clean the fresh data 
    df = pd.read_csv(input_path)
    
    # Standardize column casing dynamically to avoid key errors
    df.columns = [col.strip().capitalize() for col in df.columns]
    
    # Ensure Timestamp parsing is robust
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    # Print operational statistics to terminal
    print(f"\n[INFO] Shape of dataset: {df.shape}")
    print("\n[INFO] Data Columns & Extracted Types:")
    print(df.dtypes)
    
    # Fulfill Task 2: Save the raw csv checkpoint to data/interim/
    os.makedirs(interim_dir, exist_ok=True)
    df.to_csv(csv_output_path, index=False)
    print(f"\n[SUCCESS] Interim backup saved to: {csv_output_path}")
    
    # Fulfill Task 2: Save the clean structural file to data/processed/*.parquet
    os.makedirs(processed_dir, exist_ok=True)
    df.to_parquet(parquet_output_path, index=False)
    print(f"[SUCCESS] Task 2 Cleansed file saved to Parquet format at: {parquet_output_path}")

else:
    print(f"[ERROR] Source file missing at: {input_path}. Double-check your data directory structure.")