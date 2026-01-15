
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
import pickle

# Load data
data = pd.read_csv('data_2.csv')

# Encode categorical variables
data.replace({"Gender": {'Male': 0, 'Female': 1}}, inplace=True)
data.replace({"Workout_Type": {'Yoga': 0, 'HIIT': 1, 'Cardio': 2, 'Strength': 3}}, inplace=True)

# Create engineered features
data['Max_BPM_Range'] = data['Max_BPM'] - data['Resting_BPM']
data['Avg_BPM_Range'] = data['Avg_BPM'] - data['Resting_BPM']

# Define features
features = ['Gender', 'Age', 'Height (m)', 'Weight (kg)', 'Session_Duration (hours)',
            'Avg_BPM_Range', 'Max_BPM_Range', 'Workout_Type', 'Experience_Level']

X = data[features]
y = data["Calories_Burned"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning
gb_param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7],
    'subsample': [0.8, 0.9, 1.0]
}

gb_grid = GridSearchCV(
    GradientBoostingRegressor(random_state=42),
    gb_param_grid,
    cv=5,
    scoring='r2',
    n_jobs=-1
)

print("Training model...")
gb_grid.fit(X_train, y_train)

# Save the model
with open('calorie_model.pkl', 'wb') as f:
    pickle.dump(gb_grid.best_estimator_, f)

print("Model saved as calorie_model.pkl")
print(f"Best parameters: {gb_grid.best_params_}")
