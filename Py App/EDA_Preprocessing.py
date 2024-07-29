import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import QuantileTransformer
import joblib

# Load the datasets
train_df = pd.read_excel('data/train.xlsx')
test_df = pd.read_excel('data/test.xlsx')

# Display the top 5 rows of the training dataset
train_df.head()

train_df = train_df.convert_dtypes()
train_df
print(train_df.dtypes)

# Check for duplicate values
print(train_df.duplicated().sum())

# Check for missing values
print(train_df.isnull().sum())

# Check the data types
print('\n ---------------------------- \n \t Data Types \n ----------------------------\n')
print(train_df.dtypes)

# Summary statistics
train_df.describe()

# Plot the distribution of the target variable
sns.countplot(x='price_range', data=train_df)
plt.title('Price Range Distribution')
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(train_df.corr(), annot=True, fmt='.2f',vmin=-1, vmax=1, center=0,cmap='vlag')
plt.title('Correlation Heatmap')
plt.show()

# replacing missing values
for column in train_df.select_dtypes(include=['int64']).columns:
    if train_df[column].isnull().sum() > 0:
        train_df[column].fillna(train_df[column].mean().round(0), inplace=True)

train_df_cleaned = train_df.fillna(train_df.mean(),downcast='infer')
train_df_cleaned.head(160)

# Check for missing values
print(train_df_cleaned.isnull().sum())

qt = QuantileTransformer(n_quantiles=2000, output_distribution='normal', random_state=0)
to_standarize = ['battery_power', 'clock_speed', 'fc', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time']

train_df_cleaned[to_standarize] = qt.fit_transform(train_df_cleaned[to_standarize])

train_df_cleaned.to_csv("data/train_cleaned_feature_engineering.csv", index=False)

# Save the best model
joblib.dump(qt, 'models/qt_scaler.pkl')