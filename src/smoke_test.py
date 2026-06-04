import pandas as pd

sensor_data = {
    "temperature": 24.5,
    "humidity": 88,
    "co2": 950,
    "yield_kg": 12.4
}

df = pd.DataFrame([sensor_data])

print("Sample Polyhouse Sensor Data")
print(df)