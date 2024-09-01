from flask import Flask, render_template, request
import pandas as pd
import joblib
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Load the pre-trained model using joblib
heart_model = joblib.load(r'C:\Users\vibho\Desktop\Internal_Hackathon(Final)\FinalSetup\app\Frontend\homepage\models\heart_disease_model.sav')

# Load the dataset
heart_data = pd.read_csv(r'C:\Users\vibho\Desktop\Internal_Hackathon(Final)\FinalSetup\Backend\dataset\survey_lung_cancer.csv')

# Print column names to verify
print("Columns in DataFrame:", heart_data.columns)

# Rename columns if needed (example: trimming spaces and converting to lowercase)
heart_data.columns = heart_data.columns.str.strip().str.lower()
print("Columns in DataFrame after renaming:", heart_data.columns)

# Convert 'Male' to 0 and 'Female' to 1 if 'sex' exists
if 'sex' in heart_data.columns:
    heart_data['sex'] = heart_data['sex'].map({'Male': 0, 'Female': 1})
else:
    print("Column 'sex' not found in DataFrame")

@app.route('/', methods=['GET', 'POST'])
def heart_prediction():
    if request.method == 'POST':
        # Get user inputs
        age = float(request.form['age'])
        sex_input = request.form['sex'].lower()
        sex = 0 if sex_input == 'male' else 1
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        # Create a DataFrame with user inputs
        user_input = pd.DataFrame({
            'age': [age],
            'sex': [sex],
            'cp': [cp],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs],
            'restecg': [restecg],
            'thalach': [thalach],
            'exang': [exang],
            'oldpeak': [oldpeak],
            'slope': [slope],
            'ca': [ca],
            'thal': [thal]
        })

        # Perform prediction
        heart_prediction = heart_model.predict(user_input)

        # Determine result and image
        if heart_prediction[0] == 1:
            result = "We are really sorry to say but it seems like you have Heart Disease."
        else:
            result = "Congratulations, you don't have Heart Disease."

        return render_template('heart.html', result=result)

    return render_template('heart.html')

if __name__ == '__main__':
    app.run(debug=True)
