import pandas as pd

def run_column_smoke_test():
    print("=== STARTING COLUMN VALIDATION SMOKE TEST (NO IFS) ===")
    csv_path = "data/raw/polyhouse_sensors.csv"

    try:
        # 1. Load the dataset directly
        df = pd.read_csv(csv_path)
        print(f"SUCCESS: Read file at '{csv_path}' ({len(df)} rows detected)")

        # 2. Define the exact columns required for Task 1
        required_columns = ["timestamp", "temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]
        
        # 3. Force pandas to select these columns. 
        # If any column is missing, it will naturally throw a KeyError and jump to except.
        df_verified = df[required_columns]
        
        print("SUCCESS: All required columns are present and correctly named!")
        print(f"Verified columns: {list(df_verified.columns)}")
        print("=== SMOKE TEST: PASSED ===")
        
    except Exception as e:
        print("=== SMOKE TEST: FAILED ===")
        print(f"Validation failed. Please check your dataset columns or file path. Error: {e}")

run_column_smoke_test()