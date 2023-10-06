import requests

API_BASE_URL = "https://eventretrieval.one/api/v1"

login_data = {
    "username": "scienceaio",
    "password": "OoK9Yimi"
}
response = requests.post(f"{API_BASE_URL}/login", json=login_data)


if response.status_code == 200:
    session_id = response.json()['sessionId']
    frame = '26981'
    item = 'L09_V007'

    # Perform the SubmitAPI_with_timecode request
    params = {
        "session": session_id,
        "frame": frame,
        "item": item
    }
    response_submit = requests.get(f"{API_BASE_URL}/submit", params=params)
    if response_submit.status_code == 200:
        print("Science AIO answer is", response_submit.json()["submission"])
    else:
        print("Duplicated answer")
else:
    print("Login failed")
