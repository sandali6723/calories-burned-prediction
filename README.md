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

## 🔧 Customization

### Changing Colors
Edit the CSS variables in `index.html`:
```css
:root {
    --primary: #FF6B35;
    --secondary: #F7931E;
    --accent: #FDC830;
    /* ... */
}
```

### Adjusting Model Parameters
Edit the hyperparameter grid in `train_model.py`:
```python
gb_param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7],
    'subsample': [0.8, 0.9, 1.0]
}
```

### Changing Port
Edit the last line in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port here
```

## 🐛 Troubleshooting

### "Model not loaded" Error
- Make sure you've run `train_model.py` first
- Check that `calorie_model.pkl` exists in the directory
- Verify `data_2.csv` is available for training

### CORS Errors
- Make sure Flask-CORS is installed
- Check that the frontend is accessing the correct backend URL

### Connection Refused
- Verify the Flask server is running
- Check the port number (default: 5000)
- Ensure no firewall is blocking the connection

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

## 🎯 Future Enhancements

- Add data visualization charts
- Include workout history tracking
- Implement user accounts and profiles
- Add batch prediction for multiple workouts
- Export predictions to CSV/PDF
- Mobile app version
- Integration with fitness trackers

## 📄 License

This project is open source and available for personal and educational use.

## 🙏 Acknowledgments

- Built with Flask, Scikit-learn, and modern web technologies
- Inspired by fitness tracking and health monitoring applications

---

**Enjoy tracking your calories with CaloriBurn!** 🔥💪
