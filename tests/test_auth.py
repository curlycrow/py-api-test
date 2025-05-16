import os
import requests

API_URL = "https://example.com/api/protected"
TOKEN = os.getenv("API_TOKEN")

def test_authorized_request():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(API_URL, headers=headers)
    assert response.status_code == 200

def test_unauthorized_request():
    response = requests.get(API_URL)
    assert response.status_code == 401