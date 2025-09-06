from flask import Flask, request, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

def get_access_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "apikey": API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_input = request.json

        values = [[
            float(user_input['N']),
            float(user_input['P']),
            float(user_input['K']),
            float(user_input['temperature']),
            float(user_input['humidity']),
            float(user_input['ph']),
            float(user_input['rainfall'])
        ]]

        token = get_access_token()

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "input_data": [{
                "fields": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
                "values": values
            }]
        }

        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()

        result = response.json()
        prediction = result['predictions'][0]['values'][0][0]
        confidence_list = result['predictions'][0]['values'][0][1]
        confidence = round(max(confidence_list) * 100, 2)

        return jsonify({
            "prediction": prediction,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

