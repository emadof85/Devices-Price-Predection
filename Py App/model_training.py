import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load the datasets
train_df = pd.read_csv('data/train_cleaned_feature_engineering.csv')
test_df = pd.read_excel('data/test.xlsx')

# Data preparation

# Split the data into features and target
X = train_df.drop('price_range', axis=1)
y = train_df['price_range']

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter grid for SVC
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['rbf', 'poly', 'sigmoid']
}

# Initialize GridSearchCV with SVC
grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2, cv=5, scoring='accuracy')

# Fit the model to the data
grid.fit(X_train, y_train)

# Print the best parameters and estimator
print("Best Parameters: ", grid.best_params_)
print("Best Estimator: ", grid.best_estimator_)

# Evaluate the optimized model
best_model = grid.best_estimator_
y_pred = best_model.predict(X_val)
print(classification_report(y_val, y_pred))
print(confusion_matrix(y_val, y_pred))

joblib.dump(best_model, 'models/svc_best_model.pkl')
