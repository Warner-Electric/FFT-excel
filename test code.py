import pandas as pd
import numpy as np

# Generate a more complex dataset with wider frequency ranges
np.random.seed(42)  # For reproducibility

# Create a time series data with multiple frequency components and varying amplitudes
time = np.linspace(0, 10, 5000)
signal = (np.sin(2 * np.pi * 1 * time) * np.exp(-0.1 * time) +  # 1 Hz component with exponential decay
          np.sin(2 * np.pi * 3 * time) * np.exp(-0.05 * time) +  # 3 Hz component with slower decay
          np.sin(2 * np.pi * 5 * time) +  # 5 Hz component without decay
          np.sin(2 * np.pi * 7 * time) * np.exp(-0.02 * time) +  # 7 Hz component with very slow decay
          np.sin(2 * np.pi * 10 * time) +  # 10 Hz component without decay
          np.sin(2 * np.pi * 15 * time) +  # 15 Hz component without decay
          np.sin(2 * np.pi * 200 * time) +  # 200 Hz component without decay
          np.random.normal(0, 0.5, time.shape))  # Noise

# Create a DataFrame
df = pd.DataFrame({'Time': time, 'Signal': signal})

# Save the DataFrame to an Excel file
file_path = 'wider_frequency_ranges_dataset.xlsx'
df.to_excel(file_path, index=False, engine='openpyxl')

print(f"Dataset with wider frequency ranges saved to {file_path}")
