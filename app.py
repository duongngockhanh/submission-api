from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__, template_folder='templates')

# Read account information
with open("account.txt") as f:
    accinfo = [item.strip() for item in f.readlines()]
    acc_username = accinfo[0]
    acc_password = accinfo[1]

# Define the API base URL
API_BASE_URL = "https://eventretrieval.one/api/v1"
login_data = {
    "username": acc_username,
    "password": acc_password
}
response = requests.post(f"{API_BASE_URL}/login", json=login_data)

session_id = None
if response.status_code == 200:
    session_id = response.json()['sessionId']

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/submission", methods=['POST'])
def submission():
    submission_data = request.json
    if response.status_code == 200:
        params = {
            "session": session_id,
            "frame": submission_data['frame'],
            "item": submission_data['item']
        }
        response_submit = requests.get(f"{API_BASE_URL}/submit", params=params)
        if response_submit.status_code == 200:
            result = "Science AIO answer is " + str(response_submit.json()["submission"])
        else:
            result = "Duplicated answer"
    else:
        result = "Login failed: " + str(session_id)
    
    data = {
        'result': result
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
