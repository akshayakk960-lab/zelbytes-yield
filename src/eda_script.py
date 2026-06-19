import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/polyhouse_sensors.csv")

# Remove missing values
df = df.dropna()

# ========================================================
# NEW: Calculate and Display Specific Metrics
# ========================================================
mean_temp = df["temperature_c"].mean()
median_humidity = df["humidity_pct"].median()
max_yield = df["yield_kg"].max()
min_co2 = df["co2_ppm"].min()

print("--- Calculated Metrics ---")
print(f"Mean Temperature:  {mean_temp:.2f} °C")
print(f"Median Humidity:   {median_humidity:.2f} %")
print(f"Maximum Yield:     {max_yield:.2f} kg")
print(f"Minimum CO2:       {min_co2:.2f} ppm")
print("-" * 26)
# ========================================================

# Create 3 scatter plots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Humidity vs Yield
axes[0].scatter(df["humidity_pct"], df["yield_kg"])
axes[0].set_xlabel("Humidity (%)")
axes[0].set_ylabel("Yield (kg)")
axes[0].set_title("Humidity vs Yield")

# Temperature vs Yield
axes[1].scatter(df["temperature_c"], df["yield_kg"])
axes[1].set_xlabel("Temperature (°C)")
axes[1].set_ylabel("Yield (kg)")
axes[1].set_title("Temperature vs Yield")

# CO2 vs Yield
axes[2].scatter(df["co2_ppm"], df["yield_kg"])
axes[2].set_xlabel("CO₂ (ppm)")
axes[2].set_ylabel("Yield (kg)")
axes[2].set_title("CO₂ vs Yield")

plt.tight_layout()

# Save figure
plt.savefig("scatter_yield.png", dpi=300)

print("Scatter plots saved successfully!")