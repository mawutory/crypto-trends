import pandas as pd

# Load the trends.csv data
data = pd.read_csv("trends.csv")

# Filter the data for BTC (Bitcoin) only
btc_trend = data[data['cryptocurrency'].str.lower() == 'bitcoin']

# Select the columns to output
output = btc_trend[['week', 'cryptocurrency', 'search_interest']]

# Save the filtered data to a CSV file
output.to_csv("bitcoin_weekly_trend.csv", index=False)