import pandas as pd

# Load the prices.csv data
data = pd.read_csv("prices.csv")

# Group by 'Cryptocurrency' and calculate the standard deviation of the 'Close' column
crypto_std_dev = data.groupby('Cryptocurrency')['Close'].std()

# Create a new DataFrame with the results
output = pd.DataFrame({
    'cryptocurrency': crypto_std_dev.index,
    'standard_deviation': crypto_std_dev.round(2)  # Rounded to two decimal places
})

# Save the results to a CSV file
output.to_csv("crypto_standard_deviation.csv", index=False)