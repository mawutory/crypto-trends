import pandas as pd

# Load the prices.csv data
data = pd.read_csv("prices.csv")

# Group by 'Cryptocurrency' and sum the 'Volume' for each group
crypto_volume = data.groupby('Cryptocurrency')['Volume'].sum()

# Create a new DataFrame with the results
output = pd.DataFrame({
    'cryptocurrency': crypto_volume.index,
    'total_volume': crypto_volume.values
})

# Save the results to a CSV file
output.to_csv("total_volume_per_cryptocurrency.csv", index=False)