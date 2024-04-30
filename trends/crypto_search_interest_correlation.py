import pandas as pd

# Load trends.csv data
trends_data = pd.read_csv("trends.csv")

# Convert 'week' to datetime
trends_data['week'] = pd.to_datetime(trends_data['week'], errors='coerce')

# Filter the data to include only BTC, ETH, and BNB
target_cryptocurrencies = ["bitcoin", "ethereum", "bnb"]
trends_filtered = trends_data[trends_data['cryptocurrency'].str.lower().isin(target_cryptocurrencies)]

# Pivot the filtered data to have 'week' as index and 'cryptocurrency' as columns
trend_pivot = trends_filtered.pivot_table(index='week', columns='cryptocurrency', values='search_interest')

# Calculate the correlation matrix for BTC, ETH, and BNB
correlation_matrix = trend_pivot.corr()

# Reset the index for output
correlation_df = correlation_matrix.reset_index()

# Save the correlation results to a CSV file
correlation_df.to_csv("crypto_search_interest_correlation.csv", index=False)