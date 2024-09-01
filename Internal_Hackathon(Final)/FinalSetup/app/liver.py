from flask import Flask, render_template, request
import pandas as pd
from PIL import Image
import numpy as np
import joblib

app = Flask(__name__)

# Load the pre-trained model using joblib
liver_model = joblib.load(r'C:\Users\vibho\Desktop\Internal_Hackathon(Final)\FinalSetup\app\Frontend\homepage\models\liver_model.sav')

@app.route('/', methods=['GET', 'POST'])
def liver_prediction():
    if request.method == 'POST':
        # Get user inputs
        Sex = 0 if request.form['gender'] == 'male' else 1
        age = float(request.form['age'])
        Total_Bilirubin = float(request.form['Total_Bilirubin'])
        Direct_Bilirubin = float(request.form['Direct_Bilirubin'])
        Alkaline_Phosphotase = float(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = float(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = float(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])

        # Create a DataFrame with user inputs
        user_input = pd.DataFrame({
            'Sex': [Sex],
            'age': [age],
            'Total_Bilirubin': [Total_Bilirubin],
            'Direct_Bilirubin': [Direct_Bilirubin],
            'Alkaline_Phosphotase': [Alkaline_Phosphotase],
            'Alamine_Aminotransferase': [Alamine_Aminotransferase],
            'Aspartate_Aminotransferase': [Aspartate_Aminotransferase],
            'Total_Protiens': [Total_Protiens],
            'Albumin': [Albumin],
            'Albumin_and_Globulin_Ratio': [Albumin_and_Globulin_Ratio]
        })

        # Perform prediction
        liver_prediction = liver_model.predict(user_input)

        # Determine result and image
        if liver_prediction[0] == 1:
            result = "We are really sorry to say but it seems like you have liver disease."

        else:
            result = "Congratulations, you don't have liver disease."

        return render_template('liver.html', name=request.form['name'], result=result)

    return render_template('liver.html')

if __name__ == '__main__':
    app.run(debug=True)
