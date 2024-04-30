import pandas as pd

# Load the prices.csv data
data = pd.read_csv("prices.csv")

# Convert the 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Group by 'Cryptocurrency' to get the first and last week's closing prices for each cryptocurrency
grouped = data.groupby('Cryptocurrency')

# Get the first and last week's closing prices
first_close = grouped.first()['Close']  # First close for each cryptocurrency
last_close = grouped.last()['Close']  # Last close for each cryptocurrency

# Calculate the percentage increase
percentage_increase = ((last_close - first_close) / first_close) * 100

# Create a new DataFrame with the results
output = pd.DataFrame({
    'cryptocurrency': percentage_increase.index,
    'percentage_increase': percentage_increase.round(2)  # Round to two decimal places
})

# Save the results to a CSV file
output.to_csv("percentage_increase_price.csv", index=False)