import os
import pandas as pd

# List of cryptocurrency CSV files
cryptocurrency_files = [
    "bitcoin.csv",
    "ethereum.csv",
    "bnb.csv",
    "solana.csv",
    "xrp.csv",
    "dogecoin.csv",
    "cardano.csv",
    "polkadot.csv",
    "chainlink.csv",
    "litecoin.csv",
    "uniswap.csv",
    "filecoin.csv",
    "fetch.ai.csv",
    "monero.csv",
    "singularitynet.csv",
    "tezos.csv",
    "kucoin.csv",
    "pancakeswap.csv",
    "oasis_network.csv",
    "ocean_protocol.csv"
]

# Initialize an empty DataFrame to store consolidated data
consolidated_data = pd.DataFrame(columns=['week', 'cryptocurrency', 'search_interest'])

# Iterate over each cryptocurrency file
for file in cryptocurrency_files:
    # Read the data from the current cryptocurrency file, skipping the first row
    data = pd.read_csv(file, skiprows=1)
    
    # Extract the cryptocurrency name from the filename
    cryptocurrency = os.path.splitext(file)[0].split('-')[0]
    cryptocurrency = cryptocurrency.replace('_', ' ').title()
    
    # Ensure consistent column naming
    data.columns = ['week', 'search_interest']
    
    # Add the cryptocurrency name to the DataFrame
    data['cryptocurrency'] = cryptocurrency
    
    # Append the data to the consolidated DataFrame with all required columns
    consolidated_data = consolidated_data.append(data[['week', 'cryptocurrency', 'search_interest']], ignore_index=True)

# Save the consolidated data to a new CSV file
consolidated_data.to_csv('trends.csv', index=False)
