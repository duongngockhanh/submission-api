from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__, template_folder='templates')

# Define the API base URL
API_BASE_URL = "https://eventretrieval.one/api/v1"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Perform login using the LoginAPI
        login_data = {
            "username": "scienceaio",
            "password": "OoK9Yimi"
        }
        response = requests.post(f"{API_BASE_URL}/login", json=login_data)

        if response.status_code == 200:
            # Đăng nhập thành công, trích xuất sessionId từ phản hồi JSON
            response_json = response.json()
            session_id = response_json.get("sessionId")
            
            return redirect(url_for('dashboard'))
        else:
            # Login failed, render an error page or return an error message
            return "Login failed. Please check your credentials."

    return render_template("login.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Get the session ID, timecode, and item from the form
    session_id = request.form["session_id"]
    timecode = request.form["timecode"]
    item = request.form["item"]

    # Perform the SubmitAPI_with_timecode request
    params = {
        "session": session_id,
        "timecode": timecode,
        "item": item
    }
    response = requests.get(f"{API_BASE_URL}/submit", params=params)

    if response.status_code == 200:
        # Request successful, you can handle the response data here
        response_data = response.json()
        return jsonify(response_data)
    else:
        # Request failed, handle the error accordingly
        return "Request failed."

if __name__ == "__main__":
    app.run(debug=True)
