import pandas as pd

# Load prices.csv and trends.csv data
prices_data = pd.read_csv("../prices/prices.csv")
trends_data = pd.read_csv("trends.csv")

# Convert 'Date' and 'week' to datetime
prices_data['Date'] = pd.to_datetime(prices_data['Date'], errors='coerce')
trends_data['week'] = pd.to_datetime(trends_data['week'], errors='coerce')

# Lowercase 'Cryptocurrency' and 'cryptocurrency' for consistency
prices_data['Cryptocurrency'] = prices_data['Cryptocurrency'].str.lower()
trends_data['cryptocurrency'] = trends_data['cryptocurrency'].str.lower()

# Filter for Bitcoin in both datasets
btc_prices = prices_data[prices_data['Cryptocurrency'] == 'btc']
btc_trends = trends_data[trends_data['cryptocurrency'] == 'bitcoin']

# Merge on 'Date' and 'week'
btc_merged = pd.merge(btc_prices, btc_trends, left_on='Date', right_on='week', how='inner')

# Select relevant columns for the output
btc_weekly_trend = btc_merged[['Date', 'Close', 'search_interest']]

# Save the weekly trend for Bitcoin to a CSV file
btc_weekly_trend.to_csv("btc_weekly_price_search_trend.csv", index=False)