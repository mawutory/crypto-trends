import os
import pandas as pd

# List of cryptocurrency CSV files for price data
price_files = [
    "ADA-USD.csv",
    "AGIX-USD.csv",
    "BNB-USD.csv",
    "BTC-USD.csv",
    "CAKE-USD.csv",
    "DOGE-USD.csv",
    "DOT-USD.csv",
    "ETH-USD.csv",
    "FET-USD.csv",
    "FIL-USD.csv",
    "KCS-USD.csv",
    "LINK-USD.csv",
    "LTC-USD.csv",
    "OCEAN-USD.csv",
    "ROSE-USD.csv",
    "SOL-USD.csv",
    "UNI-USD.csv",
    "XMR-USD.csv",
    "XRP-USD.csv",
    "XTZ-USD.csv"
]

# Initialize an empty DataFrame to store consolidated price data
consolidated_price_data = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Cryptocurrency'])

# Iterate over each price CSV file
for file in price_files:
    # Read the data from the current CSV file
    data = pd.read_csv(file)
    # Extract the cryptocurrency name from the filename, removing '-USD'
    cryptocurrency = os.path.splitext(file)[0]
    cryptocurrency = cryptocurrency.split('-')[0]  # Remove the '-USD' part
    # Add a new column for the cryptocurrency name
    data['Cryptocurrency'] = cryptocurrency
    # Append the data to the consolidated DataFrame
    consolidated_price_data = consolidated_price_data.append(data, ignore_index=True)

# Save the consolidated price data to a new CSV file
consolidated_price_data.to_csv('prices.csv', index=False)