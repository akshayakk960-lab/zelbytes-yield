import pandas as pd
import os

# Change this line in your script:
file_path = "data/interim/02_cleaned.parquet"

# Check if file exists
if os.path.exists(file_path):
    # Load and sort
    df = pd.read_parquet(file_path)
    df = df.sort_values("timestamp")
    print("Success: Data loaded and sorted.")
    
    # Perform the 80/20 split
    split_idx = int(len(df) * 0.8)
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    
    # Output the split dates
    print(f"Train set: {train['timestamp'].min()} to {train['timestamp'].max()}")
    print(f"Test set: {test['timestamp'].min()} to {test['timestamp'].max()}")
    
    train.to_parquet("data/processed/train.parquet")
    test.to_parquet("data/processed/test.parquet")  
    print("Files saved to data/processed/")
else:
    print(f"Error: Could not find file at {file_path}")