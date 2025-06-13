import os
import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt

# Replace with your actual FRED API key
FRED_API_KEY = 'YOUR_FRED_API_KEY'


# Folder structure
data_dir = 'data'
figures_dir = 'figures'
os.makedirs(data_dir, exist_ok=True)
os.makedirs(figures_dir, exist_ok=True)

# File paths
data_file = os.path.join(data_dir, 'unemployment_data.csv')
figure_file = os.path.join(figures_dir, 'unemployment_trends.png')

# Load or fetch data
if not os.path.exists(data_file):
    print("Fetching data from FRED...")
    fred = Fred(api_key=FRED_API_KEY)

    series_ids = {
        'California': 'CAUR',
        'New York': 'NYUR',
        'Texas': 'TXUR',
        'United States': 'UNRATE'
    }

    data = {}
    for region, series_id in series_ids.items():
        data[region] = fred.get_series(series_id)

    df = pd.DataFrame(data)
    df.index = pd.to_datetime(df.index)

    df.to_csv(data_file)
    print(f"Data saved to {data_file}")
else:
    print(f"Reading cached data from {data_file}")
    df = pd.read_csv(data_file, index_col=0, parse_dates=True)

# Filter for recent years
df = df[df.index >= '2020-01-01']

# Plot and save figure
plt.figure(figsize=(10, 6))
df.plot()
plt.title('Unemployment Rates (2020–2025)')
plt.ylabel('Unemployment Rate (%)')
plt.xlabel('Date')
plt.grid(True)
plt.tight_layout()

# Save figure as high-res PNG (300 DPI)
plt.savefig(figure_file, dpi=300)
plt.close()

print(f"Chart saved to {figure_file}")