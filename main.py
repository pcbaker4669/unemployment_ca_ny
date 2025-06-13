from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt

# Replace with your own FRED API key
fred = Fred(api_key='YOUR_FRED_API_KEY')

# Series IDs from FRED
series_ids = {
    'California': 'CAUR',
    'New York': 'NYUR',
    'United States': 'UNRATE'
}

# Fetch data
data = {}
for region, series_id in series_ids.items():
    data[region] = fred.get_series(series_id)

# Combine into one DataFrame
df = pd.DataFrame(data)
df.index = pd.to_datetime(df.index)

# Trim to recent years (e.g., since Jan 2020)
df = df[df.index >= '2020-01-01']

# Plot
df.plot(figsize=(10, 6))
plt.title('Monthly Unemployment Rate (2020–2025)')
plt.ylabel('Unemployment Rate (%)')
plt.xlabel('Date')
plt.grid(True)
plt.legend(title='Region')
plt.tight_layout()
plt.show()
