import pandas as pd

# Load the trends.csv data
data = pd.read_csv("trends.csv")

# Filter the data for ETH (Ethereum) only
eth_trend = data[data['cryptocurrency'].str.lower() == 'ethereum']

# Select the columns to output
output = eth_trend[['week', 'cryptocurrency', 'search_interest']]

# Save the filtered data to a CSV file
output.to_csv("ethereum_weekly_trend.csv", index=False)