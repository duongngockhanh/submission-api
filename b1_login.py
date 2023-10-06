import requests


# 1. Initialize two necessary variables
API_BASE_URL = "https://eventretrieval.one/api/v1"

login_data = {
    "username": "scienceaio",
    "password": "OoK9Yimi4"
}


# 2. Post the login information - Get the response
response = requests.post(f"{API_BASE_URL}/login", json=login_data)


# 3. Parse the response
if response.status_code == 200:
    print(response.json())
    '''
    {
        'id': '9766e6e4-cfb0-4216-af11-fb0a5ddc6d22', 
        'username': 'scienceaio', 
        'role': 'PARTICIPANT', 
        'sessionId': 'node01oe09qvyf0vmja22nc1on7f2u766'
    }
    '''
else:
    print(response.json())
    '''
    {
        'description': 'Unauthorized request!', 
        'status': False
    }
    '''
