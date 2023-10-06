import requests

API_BASE_URL = "https://eventretrieval.one/api/v1"

login_data = {
    "username": "scienceaio",
    "password": "OoK9Yimi4"
}
response = requests.post(f"{API_BASE_URL}/login", json=login_data)
response_json = response.json()
if response.status_code == 200:
    print(response_json)
    '''
    {
        'id': '9766e6e4-cfb0-4216-af11-fb0a5ddc6d22', 
        'username': 'scienceaio', 
        'role': 'PARTICIPANT', 
        'sessionId': 'node01oe09qvyf0vmja22nc1on7f2u766'
    }
    '''
else:
    print(response_json)
    '''
    {
        'description': 'Unauthorized request!', 
        'status': False
    }
    '''
