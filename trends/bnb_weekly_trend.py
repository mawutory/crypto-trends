import pandas as pd

# Load the trends.csv data
data = pd.read_csv("trends.csv")

# Filter the data for BNB only
bnb_trend = data[data['cryptocurrency'].str.lower() == 'bnb']

# Select the columns to output
output = bnb_trend[['week', 'cryptocurrency', 'search_interest']]

# Save the filtered data to a CSV file
output.to_csv("bnb_weekly_trend.csv", index=False)