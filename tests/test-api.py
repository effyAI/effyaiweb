import requests
import json

url = "http://34.207.181.77/hello"
response = requests.get(url)
if response.status_code == 200:
    # Print the content of the response
    print(response.text)
else:
    # Handle errors if the request was not successful
    print(f"Request failed with status code {response.status_code}")
