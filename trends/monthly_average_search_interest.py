import pandas as pd
import numpy as np

# Load the trends.csv data
data = pd.read_csv("trends.csv")

# Replace instances of '<1' in the 'search_interest' column with 0
data['search_interest'] = data['search_interest'].replace('<1', 0).astype(float)

# Extract the year and month from the 'week' column
data['date'] = pd.to_datetime(data['week'])  # Convert 'week' to datetime
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

# Combine year and month into a new column for full date representation
data['full_month'] = pd.to_datetime(data['year'].astype(str) + '-' + data['month'].astype(str) + '-01')

# Group by 'full_month' and calculate the average search interest
monthly_avg = data.groupby('full_month')['search_interest'].mean().round(2)

# Create a new DataFrame with the formatted results
output = pd.DataFrame({
    'month': monthly_avg.index,
    'search_interest': monthly_avg.values
})

# Save the results to a CSV file
output.to_csv("monthly_average_search_interest.csv", index=False)