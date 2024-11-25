import pandas as pd
import pickle
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

# Load the CSV file into a pandas DataFrame
def load_districts():
    df = pd.read_csv('crop data rajasthan.csv')
    unique_districts = df['District'].unique().tolist()
    return unique_districts

# Load the trained model
with open('crop_recommendation_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


def get_weather_data(district):
    # Replace with the actual URL and parameters for the Weather API
    api_key = '3db767dfabd82fae2b5625524c63e079'  # Replace with your Weather.com API key
    url = 'https://api.weather.com/v3/wx/conditions/current?apiKey={api_key}&language=en-US&format=json'

    # Assuming district can be used as a location parameter
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data: {response.status_code}")
        return None
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-options', methods=['GET'])
def get_options():
    unique_districts = df['District'].unique().tolist()
    print("Unique districts:", unique_districts)  # Debugging line
    return jsonify({'districts': unique_districts})

@app.route('/get-recommendation', methods=['POST'])
def get_recommendation():

    district = request.form.get('district')
    area = float(request.form['area'])
    if 'df' not in globals():
        return jsonify({'error': 'DataFrame not loaded.'}), 500
    # Find the closest area


    # Get weather data for the district
    weather_data = get_weather_data(district)
    if weather_data:
        # Extract relevant weather features
        temperature = weather_data['temperature']  # Adjust based on actual API response
        humidity = weather_data['humidity']  # Adjust based on actual API response

        # Prepare input data for the model
        input_data = pd.DataFrame([[district, area, temperature, humidity]],
                                  columns=['District', 'Area', 'temperature', 'humidity'])

        # Make the prediction using the model
        predicted_yield = model.predict(input_data)

        # Determine the recommended crop based on the district and area
        recommended_crop = df.loc[(df['District'] == district) & (df['Area'] == area), 'Crop'].iloc[0]

        return jsonify({'recommended_crop': recommended_crop, 'predicted_yield': predicted_yield[0]})

    return jsonify({'error': 'Weather data could not be retrieved.'}), 500

if __name__ == '__main__':
    app.run(debug=True, threaded=True)