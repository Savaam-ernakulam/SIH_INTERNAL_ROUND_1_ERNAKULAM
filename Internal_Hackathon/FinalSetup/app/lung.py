from flask import Flask, render_template, request
import pandas as pd
import joblib
from PIL import Image

app = Flask(__name__)

# Load the model
lung_cancer_model = joblib.load(r'C:\Users\vibho\Desktop\Internal_Hackathon(Final)\FinalSetup\app\Frontend\homepage\models\lung_cancer_model.sav')

# Load the dataset
lung_cancer_data = pd.read_csv(r'/\FinalSetup\Backend\dataset\survey_lung_cancer.csv')

# Convert 'M' to 'Male' and 'F' to 'Female'
lung_cancer_data['GENDER'] = lung_cancer_data['GENDER'].map({'M': 'Male', 'F': 'Female'})


@app.route('/', methods = ['GET', 'POST'])
def index():
    result = ""
    image_path = ""

    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        smoking = request.form.get('smoking')
        yellow_fingers = request.form.get('yellow_fingers')
        anxiety = request.form.get('anxiety')
        peer_pressure = request.form.get('peer_pressure')
        chronic_disease = request.form.get('chronic_disease')
        fatigue = request.form.get('fatigue')
        allergy = request.form.get('allergy')
        wheezing = request.form.get('wheezing')
        alcohol_consuming = request.form.get('alcohol_consuming')
        coughing = request.form.get('coughing')
        shortness_of_breath = request.form.get('shortness_of_breath')
        swallowing_difficulty = request.form.get('swallowing_difficulty')
        chest_pain = request.form.get('chest_pain')

        # Create DataFrame with user inputs
        user_data = pd.DataFrame({
            'GENDER': [gender],
            'AGE': [age],
            'SMOKING': [smoking],
            'YELLOW_FINGERS': [yellow_fingers],
            'ANXIETY': [anxiety],
            'PEER_PRESSURE': [peer_pressure],
            'CHRONICDISEASE': [chronic_disease],
            'FATIGUE': [fatigue],
            'ALLERGY': [allergy],
            'WHEEZING': [wheezing],
            'ALCOHOLCONSUMING': [alcohol_consuming],
            'COUGHING': [coughing],
            'SHORTNESSOFBREATH': [shortness_of_breath],
            'SWALLOWINGDIFFICULTY': [swallowing_difficulty],
            'CHESTPAIN': [chest_pain]
        })

        # Map string values to numeric
        user_data.replace({'NO': 1, 'YES': 2}, inplace = True)

        # Strip leading and trailing whitespaces from column names
        user_data.columns = user_data.columns.str.strip()

        # Convert columns to numeric where necessary
        numeric_columns = ['AGE', 'FATIGUE', 'ALLERGY', 'ALCOHOLCONSUMING', 'COUGHING', 'SHORTNESSOFBREATH']
        user_data[numeric_columns] = user_data[numeric_columns].apply(pd.to_numeric, errors = 'coerce')

        # Perform prediction
        cancer_prediction = lung_cancer_model.predict(user_data)

        # Display result
        if cancer_prediction[0] == 'YES':
            result = "The model predicts that there is a risk of Lung Cancer."

        else:
            result = "The model predicts no significant risk of Lung Cancer."


    return render_template('lung_cancer.html', result = result)


if __name__ == '__main__':
    app.run(debug = True)
