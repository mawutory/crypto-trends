import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from datetime import timedelta

# Load trends.csv and create a new dataset for Bitcoin trends
trends = pd.read_csv("trends.csv")

# Filter for Bitcoin-only data
bitcoin_trends = trends[trends['cryptocurrency'].str.lower() == 'bitcoin']

# Ensure 'week' is in datetime format and sort by date
bitcoin_trends['week'] = pd.to_datetime(bitcoin_trends['week'])
bitcoin_trends = bitcoin_trends.sort_values(by='week')

# Feature engineering: create time-based features
bitcoin_trends['week_of_year'] = bitcoin_trends['week'].dt.isocalendar().week
bitcoin_trends['year'] = bitcoin_trends['week'].dt.year

# Create the target variable for next week's search_interest
bitcoin_trends['next_week_search_interest'] = bitcoin_trends['search_interest'].shift(-1)

# Drop NaNs (created by the lag feature)
bitcoin_trends_cleaned = bitcoin_trends.dropna()

# Split the data into training and testing sets
train_data, test_data = train_test_split(bitcoin_trends_cleaned, test_size=0.2, random_state=42)

# Define features and target variable
features = ['week_of_year', 'year']
target = 'next_week_search_interest'

# Train the Random Forest model
random_forest = RandomForestRegressor(n_estimators=100, random_state=42)
random_forest.fit(train_data[features], train_data[target])

# Predict the search interest for the testing data
predictions = random_forest.predict(test_data[features])

# Create a new entry for the most recent week's next week
most_recent_week = bitcoin_trends_cleaned['week'].max()
next_week = most_recent_week + timedelta(weeks=1)

# Features for the new week
next_week_features = pd.DataFrame({
    'week': [next_week],
    'week_of_year': [next_week.isocalendar().week],
    'year': [next_week.year]
})

# Predict the search interest for the next week
next_week_prediction = random_forest.predict(next_week_features[features])[0]

# Create a new record with the predicted search interest
new_record = pd.DataFrame({
    'week': [next_week],
    'search_interest': [np.nan],  # As this is unknown
    'predicted_search_interest': [next_week_prediction]
})

# Combine the existing predictions with the new prediction
predictions_df = test_data.copy()
predictions_df['predicted_search_interest'] = predictions

# Append the new record to the predictions DataFrame
combined_predictions_df = pd.concat([predictions_df, new_record], ignore_index=True)

# Save the updated predictions to a new CSV
combined_predictions_df[['week', 'search_interest', 'predicted_search_interest']].to_csv("bitcoin_search_interest_predictions_updated.csv", index=False)