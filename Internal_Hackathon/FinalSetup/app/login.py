# from flask import Flask, render_template, request, redirect, url_for, session
#
# app = Flask(__name__)
# app.secret_key = 'Hello123'  # Replace with a strong secret key
#
# # Dummy credentials for demonstration
# VALID_PHONE = "9599067655"  # Replace with a valid phone number
# VALID_PASSWORD = "password"   # Replace with a valid password
#
# @app.route('/')
# def index():
#     error_message = request.args.get('error')  # Get error message if available
#     return render_template('login.html', error_message=error_message)
#
# @app.route('/login', methods=['POST'])
# def login():
#     phone_number = request.form.get('phone_number')
#     password = request.form.get('password')
#
#     # Check credentials
#     if phone_number == VALID_PHONE and password == VALID_PASSWORD:
#         session['phone_number'] = phone_number  # Store user info in session if needed
#         return redirect(url_for('welcome'))  # Redirect to the welcome page
#     else:
#         return redirect(url_for('index', error='Invalid credentials, please try again.'))
#
# @app.route('/welcome')
# def welcome():
#     return render_template('index.html')  # Render the index.html page
#
# if __name__ == '__main__':
#     app.run(debug=True)