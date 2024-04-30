import pandas as pd

# Load the trends.csv data
data = pd.read_csv("trends.csv")

# Replace instances of '<1' in the 'search_interest' column with 0
data['search_interest'] = data['search_interest'].replace('<1', 0).astype(float)

# Group by 'cryptocurrency' and calculate the average search interest
crypto_avg = data.groupby('cryptocurrency')['search_interest'].mean().round(2)

# Create a new DataFrame with the results
output = pd.DataFrame({
    'cryptocurrency': crypto_avg.index,
    'average_search_interest': crypto_avg.values
})

# Save the results to a CSV file
output.to_csv("crypto_average_search_interest.csv", index=False)