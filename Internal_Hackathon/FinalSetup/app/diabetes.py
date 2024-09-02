from flask import Flask, render_template, request
import pandas as pd
import joblib
from PIL import Image

app = Flask(__name__)

# Load the pre-trained model using joblib
diabetes_model = joblib.load(r'C:\Users\vibho\Desktop\Internal_Hackathon(Final)\FinalSetup\app\Frontend\homepage\models\diabetes_model.sav')

@app.route('/', methods=['GET', 'POST'])
def diabetes_prediction():
    if request.method == 'POST':
        # Get user inputs
        Pregnancies = float(request.form['Pregnancies'])
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreefunction = float(request.form['DiabetesPedigreefunction'])
        Age = float(request.form['Age'])

        # Create a DataFrame with user inputs
        user_input = pd.DataFrame({
            'Pregnancies': [Pregnancies],
            'Glucose': [Glucose],
            'BloodPressure': [BloodPressure],
            'SkinThickness': [SkinThickness],
            'Insulin': [Insulin],
            'BMI': [BMI],
            'DiabetesPedigreefunction': [DiabetesPedigreefunction],
            'Age': [Age]
        })

        # Perform prediction
        diabetes_prediction = diabetes_model.predict(user_input)

        # Determine result and image
        if diabetes_prediction[0] == 1:
            result = "We are really sorry to say but it seems like you are Diabetic."
            image_file = 'positive.jpg'
        else:
            result = "Congratulations, you are not diabetic."
            image_file = 'negative.jpg'

        return render_template('diabetes.html', name=request.form['name'], result=result, image_file=image_file)

    return render_template('diabetes.html')

if __name__ == '__main__':
    app.run(debug=True)
