import pandas as pd
import joblib
import os
from sklearn.preprocessing import MinMaxScaler

def run_feature_engineering_and_split():
    # 1. Load Data
    # Ensure path matches your project structure
    df = pd.read_parquet("data/processed/02_cleaned.parquet")
    
    # 2. Sort by time (CRITICAL for time-series)
    df = df.sort_values("timestamp")
    
    # 3. Define Features and Target
    feature_cols = ["temperature_c", "humidity_pct", "co2_ppm"]
    target_col = "yield_kg"
    
    # 4. Chronological Split (80% Train, 20% Test)
    split_idx = int(len(df) * 0.8)
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    
    # 5. Leak-Free Scaling
    # Fit ONLY on training data, then transform both
    scaler = MinMaxScaler()
    
    X_train = scaler.fit_transform(train[feature_cols])
    X_test = scaler.transform(test[feature_cols])
    
    # Keep target separate
    y_train = train[target_col].values
    y_test = test[target_col].values
    
    # 6. Save Artifacts
    os.makedirs("models", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    
    # Save the scaler
    joblib.dump(scaler, "models/minmax_scaler_train.joblib")
    
    # Save processed splits
    pd.DataFrame(X_train, columns=feature_cols).to_parquet("data/processed/X_train.parquet")
    pd.DataFrame(X_test, columns=feature_cols).to_parquet("data/processed/X_test.parquet")
    
    # 7. Verification Output
    print("--- Success: Pipeline Executed ---")
    print(f"Training set: {len(X_train)} rows (Date range: {train['timestamp'].min()} to {train['timestamp'].max()})")
    print(f"Testing set: {len(X_test)} rows (Date range: {test['timestamp'].min()} to {test['timestamp'].max()})")
    print("Files saved to 'models/' and 'data/processed/'")

if __name__ == "__main__":
    run_feature_engineering_and_split()
    # Add this at the very end of your script
print("--- Pipeline completed! Files saved successfully. ---")