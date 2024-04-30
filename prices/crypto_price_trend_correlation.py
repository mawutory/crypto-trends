import pandas as pd

# Load the prices.csv data
prices_data = pd.read_csv("prices.csv")

# Convert 'Date' to datetime
prices_data['Date'] = pd.to_datetime(prices_data['Date'], errors='coerce')

# Filter the data to include only BTC, ETH, and BNB
target_cryptocurrencies = ["btc", "eth", "bnb"]
prices_filtered = prices_data[prices_data['Cryptocurrency'].str.lower().isin(target_cryptocurrencies)]

# Pivot the filtered data to have 'Date' as index and 'Cryptocurrency' as columns
price_pivot = prices_filtered.pivot_table(index='Date', columns='Cryptocurrency', values='Close')

# Calculate the correlation matrix for BTC, ETH, and BNB
correlation_matrix = price_pivot.corr()

# Reset the index for output
correlation_df = correlation_matrix.reset_index()

# Save the correlation results to a CSV file
correlation_df.to_csv("crypto_price_trend_correlation.csv", index=False)