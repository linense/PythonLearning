import requests
import json

api_url = "https://reqres.in/api/users?page=2"

# Make a request

response1 = requests.get(api_url)

print(response1.text)

# Validate Status Code

assert response1.status_code==200