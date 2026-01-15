# CaloriBurn - AI Calorie Prediction Web App

A beautiful, modern web application that predicts calories burned during workouts using a trained Gradient Boosting machine learning model.

## 🌟 Features

- **AI-Powered Predictions**: Uses a trained Gradient Boosting Regressor model
- **Beautiful UI**: Modern, animated interface with stunning visual effects
- **Real-time Results**: Instant calorie burn predictions
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Easy to Use**: Simple form-based input with clear instructions

## 📋 Prerequisites

- Python 3.8 or higher
- Your trained model data file (`data_2.csv`)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Quick Start

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train the Model

First, make sure you have your `data_2.csv` file in the same directory, then run:

```bash
python train_model.py
```

This will:
- Load and preprocess your data
- Train the Gradient Boosting model with hyperparameter tuning
- Save the trained model as `calorie_model.pkl`

### Step 3: Start the Flask Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### Step 4: Open the Web Interface

Open your web browser and navigate to:
```
http://localhost:5000
```

## 📊 Model Features

The model uses the following features to predict calories burned:

1. **Gender** (Male/Female)
2. **Age** (years)
3. **Height** (meters)
4. **Weight** (kg)
5. **Session Duration** (hours)
6. **Workout Type** (Yoga, HIIT, Cardio, Strength)
7. **Resting BPM** (beats per minute)
8. **Average BPM** (during workout)
9. **Maximum BPM** (during workout)
10. **Experience Level** (Beginner, Intermediate, Advanced)

The model automatically calculates engineered features:
- **Max BPM Range** = Max BPM - Resting BPM
- **Avg BPM Range** = Avg BPM - Resting BPM

## 🎨 Interface Overview

### Input Form
- Clean, organized form with all required workout metrics
- Dropdown menus for categorical variables
- Number inputs with appropriate ranges and step values
- Real-time validation

### Results Display
- Large, animated display of predicted calories
- Loading animation during prediction
- Error handling with user-friendly messages
- "Calculate Again" button to reset

## 🛠️ Technical Details

### Backend (Flask)
- **Framework**: Flask with CORS support
- **Model**: Scikit-learn Gradient Boosting Regressor
- **API Endpoint**: `/predict` (POST)
- **Health Check**: `/health` (GET)

### Frontend (HTML/CSS/JS)
- **Pure HTML/CSS/JS** - No frameworks required
- **Responsive Design** - Mobile-friendly
- **Animations** - Smooth transitions and effects
- **Custom Styling** - Unique, modern aesthetic

### Model Training
- **Algorithm**: Gradient Boosting Regressor
- **Hyperparameter Tuning**: GridSearchCV with cross-validation
- **Features**: 9 input features + 2 engineered features
- **Encoding**: Categorical variables mapped to numerical values

## 📝 Usage Example

1. Select your gender
2. Enter your age (e.g., 28)
3. Enter your height in meters (e.g., 1.75)
4. Enter your weight in kg (e.g., 70)
5. Enter session duration in hours (e.g., 1.5)
6. Select workout type (e.g., Cardio)
7. Enter resting BPM (e.g., 70)
8. Enter average BPM during workout (e.g., 140)
9. Enter maximum BPM reached (e.g., 156)
10. Select experience level (e.g., Intermediate)
11. Click "Predict Calories"

The model will instantly predict your calories burned!


## 📦 File Structure

```
.
├── app.py                 # Flask backend server
├── train_model.py         # Model training script
├── index.html            # Frontend web interface
├── requirements.txt      # Python dependencies
├── data_2.csv           # Your training data (required)
└── calorie_model.pkl    # Trained model (generated)
```


**Enjoy tracking your calories with CaloriBurn!** 🔥💪
