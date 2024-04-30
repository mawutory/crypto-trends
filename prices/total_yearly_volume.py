import pandas as pd

# Load the prices.csv data
data = pd.read_csv("prices.csv")

# Convert the 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract the year from the 'Date' column
data['year'] = data['Date'].dt.year

# Group by 'year' and sum the 'Volume' for each year to get the total yearly volume
yearly_volume = data.groupby('year')['Volume'].sum()

# Create a new DataFrame with the results
output = pd.DataFrame({
    'year': yearly_volume.index,
    'total_yearly_volume': yearly_volume.values
})

# Save the results to a CSV file
output.to_csv("total_yearly_volume.csv", index=False)