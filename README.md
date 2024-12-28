# SoilSense: Smart Crop Recommendation System

Welcome to the **SoilSense: Smart Crop Recommendation System** repository! This project leverages advanced deep learning techniques for soil classification and provides crop recommendations based on the soil type and weather conditions. It aims to assist farmers in making data-driven decisions to improve agricultural productivity by offering tailored suggestions for optimal crop selection.

## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **SoilSense** system uses a deep learning-based model to classify soil types from images, such as sandy, loamy, or clayey soils. Based on the identified soil type, it provides recommendations for suitable crops, taking into account various environmental factors like temperature and humidity. The system integrates real-time weather data to refine crop suggestions and make them more accurate.

The project aims to make smart agricultural decisions accessible to farmers, especially in regions with limited resources, by providing timely, data-backed guidance. The system has a simple user interface for uploading soil images and viewing the crop recommendations along with weather information.

## Objectives

1. **Soil Type Classification**:
   - Develop a Convolutional Neural Network (CNN) model to classify soil images into categories such as sandy, loamy, clayey, etc.
   
2. **Crop Recommendation Logic**:
   - Implement rule-based logic that recommends suitable crops based on the classified soil type and environmental conditions.
   
3. **Weather Data Integration**:
   - Fetch real-time weather data (temperature, humidity, etc.) via APIs to enhance the accuracy of crop recommendations.
   
4. **User Interface (UI)**:
   - Build a simple, intuitive web interface for users to upload soil images and view crop recommendations.
   
5. **Multi-Language Support**:
   - Implement multi-language support to cater to users in different regions and languages.

6. **Live Camera Integration**:
   - Allow users to capture live images of soil using their camera and upload them for classification and recommendations.

## Features

- **Real-Time Soil Type Classification**: Automatically classifies soil types from images using a trained deep learning model.
- **Crop Recommendations**: Provides a list of recommended crops based on the classified soil type.
- **Weather Data Integration**: Fetches current weather information (temperature, humidity, etc.) for the user's location to enhance crop suggestions.
- **Simple and Intuitive UI**: A web-based interface to easily upload soil images and view the recommendations.
- **Live Camera Support**: Users can take live pictures of soil and get recommendations instantly.
- **Multi-Language Support**: The system supports multiple languages to cater to users from different regions.

## Usage

1. **Soil Type Classification**: Upload a soil image via the web interface. The system classifies the soil type and displays the result.
2. **Crop Recommendations**: Based on the soil type, the system fetches crop recommendations, considering the weather data for the user’s location.
3. **Weather Data**: Users can enter their city or location to receive up-to-date weather information that impacts crop growth.
4. **Live Camera Integration**: Use your mobile or web camera to capture soil images directly for classification and recommendations.


## Installation

Follow these steps to set up and run the **SoilSense** system on your local machine.

### Step 1: Clone the Repository

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-username/SoilSense.git
cd SoilSense
```

### Step 2: Set up a Virtual Environment (Optional but Recommended)

It is recommended to set up a virtual environment to manage dependencies more efficiently.

**For Linux/Mac**:
```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Set up Model and Data

Ensure the soil classification model is saved in the project directory under the `backend` folder. If not, follow the instructions to download and place the model in the correct folder.

### Step 5: Run the Application

To run the Flask application, use the following command:

```bash
python app.py
```

### Step 6: Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

You can upload a soil image and receive crop recommendations and weather information.

---

## Technologies Used

The **SoilSense** system is built using various technologies and frameworks to provide efficient soil classification and crop recommendation.

- **Deep Learning Framework**: 
  - **TensorFlow**: Used for building and training the convolutional neural network (CNN) model for soil classification.
  - **Keras**: Provides high-level APIs for easy model building and training.

- **Web Development**: 
  - **Flask**: A lightweight Python web framework used for creating the web application.
  - **HTML, CSS, JavaScript**: These technologies are used for building the user interface and frontend of the application.

- **Weather API**: 
  - **OpenWeatherMap API**: Used for fetching real-time weather data (temperature, humidity, etc.) to enhance crop recommendations based on weather conditions.

- **Image Processing**: 
  - **Keras/TensorFlow**: Used to process and classify soil images by feeding them into the pre-trained CNN model.

- **Version Control**: 
  - **Git**: For source code management and version control.
  - **GitHub**: For hosting the project repository and collaboration.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, feel free to open an issue or submit a pull request. Your contributions will help improve the accuracy and usability of the system.

To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

Before contributing, please ensure that your changes don't break the existing functionality. You can run the app locally and verify everything works as expected.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project as per the terms of the license.

