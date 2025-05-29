import requests
import json

# API endpoint
url = "http://localhost:8000/api/annotations/"

# Request data for testing annotation creation
data = {
    "user_id": "auth0_user_123",
    "type": "point",
    "geometry": "POINT(77.1025 28.7041)",  # Make sure to use the correct WKT format
    "content": {"text": "Visited Delhi"}
}

# Make POST request to create annotation
print("Creating annotation...")
response = requests.post(url, json=data)
print(f"Status code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Make GET request to retrieve all annotations
print("\nRetrieving all annotations...")
response = requests.get(url)
print(f"Status code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2) if response.status_code == 200 else response.text}")

# Make GET request to retrieve annotations for a specific user
user_id = "auth0_user_123"
print(f"\nRetrieving annotations for user {user_id}...")
response = requests.get(f"{url}user/{user_id}")
print(f"Status code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2) if response.status_code == 200 else response.text}") 