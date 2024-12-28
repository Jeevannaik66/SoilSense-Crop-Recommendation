import os
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.preprocessing import image
import requests  # Import requests for making API calls
from io import BytesIO
from PIL import Image
import base64

# Initialize Flask application
app = Flask(__name__, template_folder=r'C:\Users\Jeevan\Documents\Projects\SoilSense\Frontend\templates')

# Paths to the model and CSV file
MODEL_PATH = r'C:\Users\Jeevan\Documents\Projects\SoilSense\Backend\soil_classification_model_mobilenet.h5'
CROP_CSV_PATH = r'C:\Users\Jeevan\Documents\Projects\SoilSense\Datasets\Crop_recommendation.csv'

# Weather API URL and Key
API_KEY = 'b95ec1dba49c758f63d36e1a685edb59'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Define class labels
class_labels = [
    'Alluvial soil',
    'Black Soil',
    'Cinder Soil',
    'Clayey soil',
    'Laterite Soil',
    'Loamy soil',
    'Peat Soil',
    'Red soil',
    'Sandy loam',
    'Sandy soil',
    'Yellow Soil'
]

# Load crop recommendations from the CSV file
def load_crop_recommendations():
    try:
        crop_data = pd.read_csv(CROP_CSV_PATH, skipinitialspace=True)
        crop_data.columns = crop_data.columns.str.strip().str.lower()  # Normalize column names

        # Organize data by soil type
        recommendations = {}
        for _, row in crop_data.iterrows():
            soil_type = row['soil type'].strip().lower()
            crop_details = {
                'crop_type': row['crop type'],
                'temperature': row['temparature'],
                'humidity': row['humidity'],
                'nitrogen': row['nitrogen'],
                'phosphorous': row['phosphorous'],
                'potassium': row['potassium'],
                'fertilizer': row['fertilizer name']
            }
            if soil_type not in recommendations:
                recommendations[soil_type] = []
            recommendations[soil_type].append(crop_details)

        return recommendations
    except Exception as e:
        print(f"Error loading crop recommendations: {e}")
        return {}

# Get weather data for the given city
def get_weather_data(city):
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric',  # To get the temperature in Celsius
        }
        response = requests.get(WEATHER_API_URL, params=params)
        weather_data = response.json()

        # Extract necessary weather details
        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            weather_description = weather_data['weather'][0]['description']
            return temperature, humidity, weather_description
        else:
            return None, None, None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None, None, None

# Load recommendations once at startup
crop_recommendations = load_crop_recommendations()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Helper function to process image from base64
def process_image_from_base64(base64_str):
    # Remove the prefix 'data:image/jpeg;base64,' or similar
    base64_str = base64_str.split(',')[1]
    img_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_data))
    img = img.resize((224, 224))  # Resize the image for the model
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image
    return img_array

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    file = None

    # Check if a file is uploaded
    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
    # Check if the image is captured via the camera (base64)
    elif 'captured_image' in request.form and request.form['captured_image']:
        captured_image = request.form['captured_image']
        img_array = process_image_from_base64(captured_image)
    else:
        return render_template('index.html', error="No file or captured image provided")

    # If an image file is uploaded
    if file:
        # Save the uploaded file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Load and preprocess the image
        img = image.load_img(file_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image

    # Make predictions
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class = class_labels[predicted_class_index].lower().strip()  # Normalize for lookup

    # Get crop recommendations for the predicted soil type
    soil_crops = crop_recommendations.get(predicted_class, [])
    if not soil_crops:
        return render_template('index.html', error=f"No data available for soil type: {predicted_class}")

    # Extract crop names to display
    crop_names = list({crop['crop_type'] for crop in soil_crops})

    # Get weather data for the city entered by the user
    city = request.form.get('city')
    temperature, humidity, description = get_weather_data(city)

    # Render the crop options for the predicted soil type and weather information
    return render_template(
        'index.html',
        soil_type=predicted_class.title(),
        crops=crop_names,
        uploaded_image=file.filename if file else None,
        city=city,
        temperature=temperature,
        humidity=humidity,
        description=description
    )

# Route for showing crop details
@app.route('/crop_details', methods=['POST'])
def crop_details():
    crop_type = request.form.get('crop_type')
    soil_type = request.form.get('soil_type').lower()

    # Find the crop details
    selected_crop = next((crop for crop in crop_recommendations.get(soil_type, []) if crop['crop_type'] == crop_type), None)
    if not selected_crop:
        return jsonify({"error": "Crop details not found"}), 404

    return render_template(
        'index.html',
        crop_info={ 
            'Soil Type': soil_type.title(),
            'Crop Type': selected_crop['crop_type'],
            'Temperature': selected_crop['temperature'],
            'Humidity': selected_crop['humidity'],
            'Nitrogen': selected_crop['nitrogen'],
            'Phosphorous': selected_crop['phosphorous'],
            'Potassium': selected_crop['potassium'],
            'Fertilizer Name': selected_crop['fertilizer']
        }
    )

if __name__ == "__main__":
    app.run(debug=True)
