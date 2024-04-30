import pandas as pd

# Load the trends.csv data
data = pd.read_csv("trends.csv")

# Convert 'search_interest' to numeric, replacing non-numeric values
data['search_interest'] = pd.to_numeric(data['search_interest'], errors='coerce')

# Drop NaN values (if any) resulting from conversion errors
data = data.dropna(subset=['search_interest'])

# Group by 'cryptocurrency' to calculate the range (maximum - minimum) of 'search_interest'
crypto_range = data.groupby('cryptocurrency')['search_interest'].agg(['min', 'max'])

# Convert 'min' and 'max' to numeric to ensure correct operations
crypto_range['min'] = pd.to_numeric(crypto_range['min'])
crypto_range['max'] = pd.to_numeric(crypto_range['max'])

# Calculate the range
crypto_range['range'] = crypto_range['max'] - crypto_range['min']

# Create a new DataFrame with the results
output = pd.DataFrame({
    'cryptocurrency': crypto_range.index,
    'range': crypto_range['range'].round(2)  # Rounded to two decimal places
})

# Save the results to a CSV file
output.to_csv("crypto_search_interest_range.csv", index=False)
