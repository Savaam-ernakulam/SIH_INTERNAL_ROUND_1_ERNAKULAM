from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
model_path = r'C:\Users\vibho\Desktop\Internal_Hackathon(Final)\FinalSetup\app\Frontend\homepage\models\chronic_model.sav'
try:
    chronic_disease_model = joblib.load(model_path)
except Exception as e:
    print(f"Error loading the model: {e}")
    chronic_disease_model = None

@app.route('/')
def index():
    return render_template('chronic_kidney.html')

@app.route('/chronic_kidney', methods=['GET', 'POST'])
def predict_chronic_kidney():
    if request.method == 'POST':
        try:
            # Collect form data and handle possible errors
            data = {
                'age': [float(request.form.get('age', 0))],
                'bp': [float(request.form.get('bp', 0))],
                'sg': [float(request.form.get('sg', 0))],
                'al': [float(request.form.get('al', 0))],
                'su': [float(request.form.get('su', 0))],
                'rbc': [1 if request.form.get('rbc') == "Normal" else 0],
                'pc': [1 if request.form.get('pc') == "Normal" else 0],
                'pcc': [1 if request.form.get('pcc') == "Present" else 0],
                'ba': [1 if request.form.get('ba') == "Present" else 0],
                'bgr': [float(request.form.get('bgr', 0))],
                'bu': [float(request.form.get('bu', 0))],
                'sc': [float(request.form.get('sc', 0))],
                'sod': [float(request.form.get('sod', 0))],
                'pot': [float(request.form.get('pot', 0))],
                'hemo': [float(request.form.get('hemo', 0))],
                'pcv': [float(request.form.get('pcv', 0))],
                'wc': [float(request.form.get('wc', 0))],
                'rc': [float(request.form.get('rc', 0))],
                'htn': [1 if request.form.get('htn') == "Yes" else 0],
                'dm': [1 if request.form.get('dm') == "Yes" else 0],
                'cad': [1 if request.form.get('cad') == "Yes" else 0],
                'appet': [1 if request.form.get('appet') == "Good" else 0],
                'pe': [1 if request.form.get('pe') == "Yes" else 0],
                'ane': [1 if request.form.get('ane') == "Yes" else 0]
            }

            user_input = pd.DataFrame(data)

            if chronic_disease_model is not None:
                prediction = chronic_disease_model.predict(user_input)
                if prediction[0] == 1:
                    result = "We are really sorry to say but it seems like you have kidney disease."
                else:
                    result = "Congratulations, You don't have kidney disease."
            else:
                result = "Model not loaded properly. Please try again later."

            print(result)
            return render_template('chronic_kidney.html', result = result)

        except Exception as e:
            result = f"Error in processing your input: {e}"
            return render_template('chronic_kidney.html', result=result)

    return render_template('chronic_kidney.html')

if __name__ == '__main__':
    app.run(debug=True)
