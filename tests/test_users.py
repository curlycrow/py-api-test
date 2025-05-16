import requests

def test_get_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2
    assert "email" in data["data"]

def test_response_structure():
    response = requests.get("https://reqres.in/api/users/2")
    body = response.json()

    assert "data" in body
    assert isinstance(body["data"]["email"], str)
    assert body["data"]["email"].endswith("@reqres.in")