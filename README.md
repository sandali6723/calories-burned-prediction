Calories Burn Prediction – Machine Learning Model

This branch contains the complete machine learning pipeline for predicting calories burned during workouts.
It focuses on data preparation, model selection, training, evaluation, and documentation, independent of application deployment.

📌 Branch Purpose

The ML model branch is dedicated to:

Exploratory data analysis (EDA)

Feature engineering

Training multiple regression models

Comparing model performance

Selecting the best-performing model

Saving the trained model for deployment

The trained model from this branch is later used in the app branch.

📂 Contents of This Branch

📊 Dataset used for training and testing

📓 Jupyter notebooks / Python scripts for:

Data preprocessing

Model training

Model evaluation

📈 Performance comparison results

📄 Research paper / documentation

💾 Final trained model file (.pkl)

📊 Dataset Description

The dataset includes workout and physiological parameters such as:

Gender

Age

Height

Weight

Workout duration

Workout type

Resting heart rate

Average heart rate

Maximum heart rate

Experience level

Target Variable

Calories burned

🔧 Data Preprocessing

The following preprocessing steps were applied:

Handling missing values

Encoding categorical variables

Feature scaling where required

Feature engineering to improve model performance

Engineered features include:

Heart rate range values derived from resting, average, and maximum BPM

🤖 Models Evaluated

Multiple regression models were trained and evaluated, including:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

🏆 Model Selection

✅ Selected Model: Gradient Boosting Regressor

Reason for selection:

Achieved the highest prediction accuracy

Better generalization on unseen data

Strong performance on non-linear relationships

Reduced overfitting compared to simpler models

📈 Model Evaluation

The models were evaluated using standard regression metrics:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score

Cross-validation and hyperparameter tuning were applied to improve reliability and robustness.
