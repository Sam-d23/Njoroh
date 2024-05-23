import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Generate time series data for one day at 1-minute intervals
time = [datetime.now() - timedelta(minutes=i) for i in range(1440)]
time.reverse()

# Simulate solar irradiance (W/m^2), temperature (°C), voltage (V), current (A)
irradiance = [max(0, 1000 * np.sin(np.pi * (t.hour * 60 + t.minute) / 720)) for t in time]
temperature = [20 + 10 * np.sin(np.pi * (t.hour * 60 + t.minute) / 720 + np.pi / 4) for t in time]
voltage = [30 + 0.05 * irr for irr in irradiance]
current = [irr / 1000 * 8 for irr in irradiance]

# Combine into a DataFrame
data = pd.DataFrame({'Time': time, 'Irradiance': irradiance, 'Temperature': temperature, 'Voltage': voltage, 'Current': current})

# Save to CSV for further use
data.to_csv('solar_data.csv', index=False)

