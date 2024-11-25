import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import requests

def get_weather(district):
    """Fetches temperature and humidity from OpenWeatherMap API."""
    api_key = "74971c9629dd4c0c8b3194700d13d7aa"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    district = district + ", IN"
    complete_url = base_url + "appid=" + api_key + "&q=" + district
    response = requests.get(complete_url)
    data = response.json()

    if "main" in data:
        main = data["main"]
        temperature = main.get("temp", None)
        humidity = main.get("humidity", None)
        if temperature is not None:
          temperature = temperature -273.15
        return temperature, humidity
    else:
        print(f"City Not Found: {district}")
        return None, None

# Load the CSV file
df = pd.read_csv('crop data rajasthan.csv')

# Handle missing values (if any)
df = df.fillna(method = 'ffill')

# ----> Get all column names from the DataFrame <----
all_columns = df.columns.tolist()

# ----> Define a list of all crop names <----
crop_names = ['coriander', 'dry chillies', 'garlic', 'onion', 'potato', 'sugarcane', 'sweet potato',
              'guar seed', 'sun hemp', 'tapioca', 'citrus fruit', 'mango', 'other fresh fruits',
              'other vegetables', 'pome fruit', 'other oilseeds', 'ginger', 'banana', 'tobacco',
              'papaya', 'watermelon', 'turmeric', 'grapes', 'orange']

# ----> Filter for crop columns based on the defined crop names and suffixes <----
crop_columns = [col for col in all_columns if any(crop in col for crop in crop_names) and any(suffix in col for suffix in ['_Area', '_Production', '_Yield'])]

# Encode categorical variables
label_encoder = LabelEncoder()
df['District'] = label_encoder.fit_transform(df['District'])

# Fetch weather data for each district
weather_data = []
for district in df['District'].unique():
    temperature, humidity = get_weather(label_encoder.inverse_transform([district])[0])
    weather_data.append((temperature, humidity))

# Create a DataFrame for weather data
weather_df = pd.DataFrame(weather_data, columns=['Temperature', 'Humidity'])
weather_df['District'] = df['District'].unique()

# Merge weather data with the original DataFrame
df = df.merge(weather_df, on='District', how='left')

# ----> Assuming 'Year' column contains values like '1998 - 1999', we'll take the first year <----
df['Year'] = df['Year'].str.split(' - ').str[0].astype(int)

# Create the feature set and target variables
X = df[['District', 'Year', 'Temperature', 'Humidity'] + [col for col in crop_columns if col.endswith(('_Area', '_Production'))]]
y = df[[col for col in crop_columns if col.endswith('_Yield')]]

# Scale numerical features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open('crop_recommendation_model.pkl', 'wb') as file:
    pickle.dump(model, file)
