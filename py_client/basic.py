import requests

endpoint = "http://Localhost:8000/api/"

get_response = requests.get(endpoint,params={"abs": 123},json={"query": "Hello World"})
# print(get_response.text)
print(get_response.status_code)
print(get_response.json())
