import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.predict import predict_yield

# 1. Page Configuration
st.set_page_config(
    page_title="Mushroom Yield Forecast", 
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Polyhouse Yield Predictor")
st.caption("Agritech environmental forecasting from sensor data")

# 2. Optimized Cache for Model Pipeline
@st.cache_resource
def get_prediction_pipeline():
    """
    Caches the prediction function resource so the model 
    doesn't reload from disk on subsequent slider adjustments.
    """
    return predict_yield

# Instantiate cached function
cached_predict = get_prediction_pipeline()

# 3. Sidebar Inputs for Polyhouse Sensors
with st.sidebar:
    st.header("Sensor Readings")
    temp = st.slider("Temperature (°C)", 10.0, 35.0, 22.0, 0.1)
    humid = st.slider("Humidity (%)", 50.0, 100.0, 88.0, 0.5)
    co2 = st.slider("CO₂ (ppm)", 400, 2000, 900, 10)

# 4. Main Panel Layout & Prediction Action
st.subheader("Current Readings Evaluation")

if st.button("Predict Yield", type="primary"):
    with st.spinner("Running inference pipeline..."):
        try:
            # Pass exactly the 3 required positional arguments
            raw_kg = cached_predict(temp, humid, co2)
            
            # Post-processing safeguard against edge-case negative weights
            display_kg = max(0.0, raw_kg)
            
            # Output metrics to UI
            st.metric(label="Estimated Daily Yield", value=f"{display_kg:.2f} kg")
            st.success("Yield calculations updated successfully!")
            
        except Exception as e:
            st.error("🚨 The App Failed to Run Inference")
            st.markdown(f"**Error Message:** `{e}`")
            st.info("Please verify your 'models/' folder contains your trained joblib files and 'src/predict.py' is functional.")

# 5. Requirement Requirement Check: Interactive Sensitivity Chart
st.markdown("---")
st.subheader("Temperature Sensitivity Analysis")
st.write("Visualizing predicted yield patterns across varying temperatures using current humidity and CO₂ levels.")

try:
    # Generate 50 hypothetical temperature variations to plot a trend curve
    temp_range = np.linspace(10.0, 35.0, 50)
    predicted_yields = [cached_predict(t, humid, co2) for t in temp_range]

    # Render Trend Line using Matplotlib
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(temp_range, predicted_yields, color="#00d2ff", linewidth=2.5, label="Yield Curve")
    ax.axvline(x=temp, color="#ff007f", linestyle="--", alpha=0.8, label=f"Selected Temp ({temp}°C)")
    
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Yield (kg)")
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend()
    
    # Render plot safely inside Streamlit
    st.pyplot(fig)
except Exception as e:
    st.warning(f"Could not render sensitivity plot: {e}")