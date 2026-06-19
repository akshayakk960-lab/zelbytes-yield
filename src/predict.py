# src/predict.py
import json
import joblib
from pathlib import Path

# 1. Keep this as "models" since your terminal is executing from the inner folder
MODEL_DIR = Path("models")

def load_artifacts():
    """
    Safely loads the serialized model, scaler, and feature tracking files.
    """
    try:
        scaler = joblib.load(MODEL_DIR / "minmax_scaler_train.joblib")
        
        # 2. CHANGED HERE: Match your actual file name 'champion.joblib'
        model = joblib.load(MODEL_DIR / "champion.joblib") 
        
        feature_cols = json.loads((MODEL_DIR / "feature_cols.json").read_text())
        return scaler, model, feature_cols
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Missing ML artifact in 'models/' directory. Detailed Error: {e}"
        )

# Initialize components
_scaler, _model, _feature_cols = load_artifacts()

def predict_yield(temperature_c: float, humidity_pct: float, co2_ppm: float) -> float:
    row = [[temperature_c, humidity_pct, co2_ppm]]
    scaled_row = _scaler.transform(row)
    prediction = _model.predict(scaled_row)
    return float(prediction[0])