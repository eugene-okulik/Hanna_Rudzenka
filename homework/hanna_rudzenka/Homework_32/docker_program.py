import requests
import time

try:
    start_time = time.time()
    response = requests.get('https://www.google.com/')
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert 'Google' in response.text
    assert response.status_code == 200
    print(f"Response time: {elapsed_time:.2f} seconds")
    print("test finished")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
