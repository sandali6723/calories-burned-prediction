from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Load the trained model (you'll need to train it first using train_model.py)
MODEL_PATH = 'calorie_model.pkl'

try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Warning: Model file '{MODEL_PATH}' not found. Please train the model first.")
    model = None

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first using train_model.py'
        }), 500
    
    try:
        # Get data from request
        data = request.json
        
        # Extract features
        gender = 0 if data['gender'] == 'Male' else 1
        age = float(data['age'])
        height = float(data['height'])
        weight = float(data['weight'])
        session_duration = float(data['session_duration'])
        max_bpm = float(data['max_bpm'])
        avg_bpm = float(data['avg_bpm'])
        resting_bpm = float(data['resting_bpm'])
        
        # Map workout type
        workout_map = {'Yoga': 0, 'HIIT': 1, 'Cardio': 2, 'Strength': 3}
        workout_type = workout_map[data['workout_type']]
        
        experience_level = int(data['experience_level'])
        
        # Calculate engineered features
        max_bpm_range = max_bpm - resting_bpm
        avg_bpm_range = avg_bpm - resting_bpm
        
        # Create feature array in correct order
        features = np.array([[
            gender, age, height, weight, session_duration,
            avg_bpm_range, max_bpm_range, workout_type, experience_level
        ]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        return jsonify({
            'calories_burned': round(prediction, 2)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
