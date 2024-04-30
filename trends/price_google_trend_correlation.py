import pandas as pd

# Load prices.csv and trends.csv
prices_data = pd.read_csv("../prices/prices.csv")
trends_data = pd.read_csv("trends.csv")

# Convert 'Date' and 'week' to datetime and check for consistency
prices_data['Date'] = pd.to_datetime(prices_data['Date'], errors='coerce')
trends_data['week'] = pd.to_datetime(trends_data['week'], errors='coerce')

# Ensure consistent lowercase formatting
prices_data['Cryptocurrency'] = prices_data['Cryptocurrency'].str.lower()
trends_data['cryptocurrency'] = trends_data['cryptocurrency'].str.lower()

# Apply the mapping for consistency
trend_to_token_mapping = {
    "bitcoin": "btc",
    "bnb": "bnb",
    "cardano": "ada",
    "chainlink": "link",
    "dogecoin": "doge",
    "ethereum": "eth",
    "fetch.ai": "fet",
    "filecoin": "fil",
    "kucoin": "kcs",
    "litecoin": "ltc",
    "monero": "xmr",
    "oasis network": "rose",
    "ocean protocol": "ocean",
    "pancakeswap": "cake",
    "polkadot": "dot",
    "singularitynet": "agix",
    "solana": "sol",
    "tezos": "xtz",
    "uniswap": "uni",
    "xrp": "xrp"
}

# Map 'cryptocurrency' in trends.csv
trends_data['cryptocurrency'] = trends_data['cryptocurrency'].map(trend_to_token_mapping)

# Drop NaNs to avoid alignment issues
prices_data.dropna(subset=['Date', 'Cryptocurrency'], inplace=True)
trends_data.dropna(subset=['week', 'cryptocurrency'], inplace=True)

# Merge datasets with an inner join to ensure only matching rows
merged_data = pd.merge(
    prices_data,
    trends_data,
    left_on=['Date', 'Cryptocurrency'],
    right_on=['week', 'cryptocurrency'],
    how='inner'
)

# Diagnose overlapping data to ensure variation
if merged_data.empty:
    print("No overlapping data. Check date ranges or mapping alignment.")
else:
    print("Sample of merged data:")
    print(merged_data[['Date', 'Cryptocurrency', 'week', 'cryptocurrency', 'Close', 'search_interest']].head(10))

    # Calculate the correlation only if there's sufficient variation
    correlation_results = merged_data.groupby('Cryptocurrency')[['Close', 'search_interest']].corr().iloc[0::2, -1]

    # Ensure there's no perfect correlation due to identical data
    if correlation_results.isna().any():
        print("Potential data issues detected. Review source data for identical values.")

    # Create the DataFrame with correlation values
    correlation_df = pd.DataFrame({
        'cryptocurrency': correlation_results.index.get_level_values(0),
        'price_google_trend_correlation': correlation_results.values.round(2)
    })

    # Save the results to a CSV file
    correlation_df.to_csv("price_google_trend_correlation.csv", index=False)
