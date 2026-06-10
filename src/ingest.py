import pandas as pd
import os

def load_to_interim_pipeline():
    print("=== STARTING TASK 1: INGESTION PIPELINE ===")
    
    # Define our source and destination paths
    raw_path = "data/raw/polyhouse_sensors.csv"
    interim_dir = "data/interim"
    processed_dir = "data/processed"
    
    # Make sure the target folders exist
    os.makedirs(interim_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)
    
    try:
        # 1. READ FROM RAW
        df = pd.read_csv(raw_path)
        print(f"SUCCESS: Read raw file with {len(df)} rows.")
        
        # 2. LOAD TO INTERIM (Save a raw copy to interim folder as requested)
        interim_path = f"{interim_dir}/01_loaded.csv"
        df.to_csv(interim_path, index=False)
        print(f"SUCCESS: Loaded and saved raw copy to interim: '{interim_path}'")
        
        # 3. CLEAN & SAVE TO PROCESSED
        # Ensure column headers are neat and lowercase
        df.columns = df.columns.str.strip().str.lower()
        
        processed_path = f"{processed_dir}/02_cleaned.parquet"
        df.to_parquet(processed_path, index=False)
        print(f"SUCCESS: Cleaned data saved to processed: '{processed_path}'")
        print("=== INGESTION TASK COMPLETE ===")
        
    except Exception as e:
        print("=== INGESTION TASK FAILED ===")
        print(f"Error during ingestion execution: {e}")

    load_to_interim_pipeline()