import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# Load trends.csv and create a new dataset for Bitcoin trends
trends = pd.read_csv("trends.csv")

# Filter the dataset for Bitcoin only
bitcoin_trends = trends[trends['cryptocurrency'].str.lower() == 'bitcoin']

# Ensure 'week' is in datetime format and sort by date
bitcoin_trends['week'] = pd.to_datetime(bitcoin_trends['week'])
bitcoin_trends = bitcoin_trends.sort_values(by='week')

# Feature engineering: create time-based features (like week of year)
bitcoin_trends['week_of_year'] = bitcoin_trends['week'].dt.isocalendar().week
bitcoin_trends['year'] = bitcoin_trends['week'].dt.year

# Lag feature for next week's search_interest (target variable)
bitcoin_trends['next_week_search_interest'] = bitcoin_trends['search_interest'].shift(-1)

# Drop NaNs (created by the lag feature)
bitcoin_trends_cleaned = bitcoin_trends.dropna()

# Split the dataset into training and testing sets (80% train, 20% test)
train_data, test_data = train_test_split(bitcoin_trends_cleaned, test_size=0.2, random_state=42)

# Define the features and target variable for training
features = ['week_of_year', 'year']  # You can add more features if needed
target = 'next_week_search_interest'

# Train Linear Regression model
linear_reg = LinearRegression()
linear_reg.fit(train_data[features], train_data[target])

# Train Random Forest Regressor
random_forest = RandomForestRegressor(n_estimators=100, random_state=42)
random_forest.fit(train_data[features], train_data[target])

# Train Gradient Boosting Regressor
gradient_boosting = GradientBoostingRegressor(n_estimators=100, random_state=42)
gradient_boosting.fit(train_data[features], train_data[target])

# Predictions and evaluation on the test set
models = {
    "Linear Regression": linear_reg,
    "Random Forest": random_forest,
    "Gradient Boosting": gradient_boosting
}

results = []

for model_name, model in models.items():
    # Make predictions
    predictions = model.predict(test_data[features])
    
    # Calculate RMSE
    rmse = np.sqrt(mean_squared_error(test_data[target], predictions))
    
    results.append({"Model": model_name, "RMSE": rmse})

# Create a DataFrame for evaluation results and save to CSV
evaluation_df = pd.DataFrame(results)
evaluation_df.to_csv("model_evaluation.csv", index=False)