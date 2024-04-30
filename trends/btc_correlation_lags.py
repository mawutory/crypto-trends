import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv("btc_scatter_plot_data.csv")

# Ensure 'Date' is in datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Initialize an empty list to store correlations for different time lags
correlation_lags = []

# Define the range of time lags to explore (e.g., from -10 to +10)
for lag in range(-10, 11):  # Exploring lags from -10 to +10
    # Shift 'search_interest' by the specified lag
    data['shifted_interest'] = data['search_interest'].shift(lag)
    
    # Drop NaNs to ensure valid data for correlation
    cleaned_data = data[['Close', 'shifted_interest']].dropna()

    # Calculate correlation only if there's enough data
    if len(cleaned_data) > 1:  # Ensure there's at least two data points
        correlation = cleaned_data.corr(numeric_only=True).iloc[0, 1]
    else:
        correlation = np.nan  # Set to NaN if there's not enough valid data
    
    # Append the lag and the corresponding correlation to the list
    correlation_lags.append({'lag': lag, 'correlation': correlation})

# Create a DataFrame with the correlation results for each lag
correlation_lag_df = pd.DataFrame(correlation_lags)

# Find the lag with the highest correlation
ideal_lag = correlation_lag_df['correlation'].idxmax()
best_correlation = correlation_lag_df.loc[ideal_lag, 'correlation']

# Save the results to a CSV file
correlation_lag_df.to_csv("btc_correlation_lags.csv", index=False)

print("Ideal time lag with highest correlation:", ideal_lag - 10)  # Adjusting for index shift
print("Highest correlation:", best_correlation)
