import pandas as pd

# Load the prices.csv data
data = pd.read_csv("prices.csv")

# Convert the 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract the year from the 'Date' column
data['year'] = data['Date'].dt.year

# Group by 'year' and 'cryptocurrency', then get the last closing price for each year
yearly_close = data.groupby(['year', 'Cryptocurrency']).apply(lambda x: x.iloc[-1]['Close']).reset_index()

# Rename the columns to provide clarity
yearly_close.columns = ['year', 'cryptocurrency', 'close_price']

# Save the results to a CSV file
yearly_close.to_csv("yearly_close_price.csv", index=False)