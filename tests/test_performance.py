import time
import requests

def test_performance():
    start = time.time()
    response = requests.get("https://reqres.in/api/users/2")
    duration = time.time() - start

    assert duration < 0.5, f"Response too slow: {duration}s"
    assert response.status_code == 200