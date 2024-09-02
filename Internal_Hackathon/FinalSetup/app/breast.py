from flask import Flask, request, render_template
import pandas as pd
import joblib
from io import BytesIO
from PIL import Image
import base64

app = Flask(__name__)

# Load the model
breast_cancer_model = joblib.load(r'C:\Users\vibho\Desktop\Internal_Hackathon(Final)\FinalSetup\app\Frontend\homepage\models\breast_cancer.sav')

# Load the dataset
breast_cancer_data = pd.read_csv(r'/\FinalSetup\Backend\dataset\Breast_Cancer_Dataset.csv')


@app.route('/')
def index():
    return render_template('breast_cancer.html')


@app.route('/breast', methods = ['GET', 'POST'])
def predict_breast_cancer():
    # Collect form data
    data = {
        'radius_mean': [float(request.form['radius_mean'])],
        'texture_mean': [float(request.form['texture_mean'])],
        'perimeter_mean': [float(request.form['perimeter_mean'])],
        # Add more fields as necessary
    }

    # Create DataFrame
    user_input = pd.DataFrame(data)

    # Predict
    prediction = breast_cancer_model.predict(user_input)

    # Determine result and image
    if prediction[0] == 1:
        result = "The model predicts that you have Breast Cancer."
        image_path = 'positive.jpg'
    else:
        result = "The model predicts that you don't have Breast Cancer."
        image_path = 'negative.jpg'

    # Open image and encode to base64
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

    return render_template('breast_cancer.html', result = result, image_data = img_base64)


if __name__ == '__main__':
    app.run(debug = True)
