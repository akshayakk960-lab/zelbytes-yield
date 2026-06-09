import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for aesthetics
sns.set_theme(style="darkgrid")

# Ensure the output directory exists
output_dir = 'reports/figures'
os.makedirs(output_dir, exist_ok=True)

# 1. Load the processed data
input_path = 'data/processed/02_cleaned.parquet'

if os.path.exists(input_path):
    df = pd.read_parquet(input_path)
else:
    input_path = 'data/interim/01_loaded.csv'
    df = pd.read_csv(input_path)

# FORCE ALL COLUMN NAMES TO BE UPPERCASE TO PREVENT KEYERRORS
df.columns = [col.strip().upper() for col in df.columns]

print("--- Data Loaded Successfully ---")
print(f"Normalized columns in dataset: {list(df.columns)}")

# 2. Print Data Quality & Descriptive Statistics 
print("\n--- Data Quality Summary ---")
print(f"Date Range: {df['TIMESTAMP'].min()} to {df['TIMESTAMP'].max()}")
print(f"Missing Values: {df.isnull().sum().sum()}")

print("\n--- Descriptive Statistics ---")
columns_to_show = ['YIELD', 'HUMIDITY', 'CO2', 'TEMPERATURE']
print(df[columns_to_show].describe().loc[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']])

# 3. Generate and Save Plots

# Plot 1: CO2 vs Yield
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='CO2', y='YIELD', color='purple', alpha=0.7)
plt.title('CO2 vs. Crop Yield')
plt.xlabel('CO2 Levels')
plt.ylabel('Yield')
plt.savefig(f'{output_dir}/co2_vs_yield.png', bbox_inches='tight')
plt.close()

# Plot 2: Humidity vs Yield
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='HUMIDITY', y='YIELD', color='blue', alpha=0.7)
plt.title('Humidity vs. Crop Yield')
plt.xlabel('Humidity (%)')
plt.ylabel('Yield')
plt.savefig(f'{output_dir}/humidity_vs_yield.png', bbox_inches='tight')
plt.close()

# Plot 3: Temperature vs Yield
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='TEMPERATURE', y='YIELD', color='orange', alpha=0.7)
plt.title('Temperature vs. Crop Yield')
plt.xlabel('Temperature (°C)')
plt.ylabel('Yield')
plt.savefig(f'{output_dir}/temperature_vs_yield.png', bbox_inches='tight')
plt.close()

# Plot 4: Correlation Heatmap
plt.figure(figsize=(6, 4))
numerical_cols = df[['YIELD', 'HUMIDITY', 'CO2', 'TEMPERATURE']]
sns.heatmap(numerical_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.savefig(f'{output_dir}/correlation_heatmap.png', bbox_inches='tight')
plt.close()

print(f"\n--- All 4 Figures Saved in {output_dir}/ ---")