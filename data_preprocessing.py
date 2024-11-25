import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the CSV file
df = pd.read_csv('crop data rajasthan.csv')

# Handle missing values
df = df.fillna(method='ffill')

# Identify the crop columns
crop_columns = [col for col in df.columns if '_' in col]

# Encode categorical variables
label_encoder = LabelEncoder()
df['District'] = label_encoder.fit_transform(df['District'])

# Create the feature set and target variables
X = df[['District'] + [f'{crop}_{metric}' for crop in crop_columns for metric in ['area', 'production']]]
y = df[[f'{crop}_yield' for crop in crop_columns]]

# Save the preprocessed data
X.to_csv('X.csv', index=False)
y.to_csv('y.csv', index=False)
