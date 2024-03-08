# app1.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input factors from the form
    factor1 = float(request.form['factor1'])

    # Define your criteria for prediction
    if factor1 <= 2:
        predicted_performance = "Low"
    else:
        predicted_performance = "High"

    # Render the result template with the predicted performance
    return render_template('result.html', predicted_performance=predicted_performance)

if __name__ == '__main__':
    app.run(debug=True)
