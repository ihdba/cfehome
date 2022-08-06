import requests


# endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"


get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello Worlds"}) # HTTP Request

# print(get_response.text) # print raw text response
print(get_response.json()) # print raw text response
# print(get_response.status_code) 

# HTTP Request -> HTML
# REST API HTTP REQUEST -> JSON
# JavaScript Object Notation  ~ Python Dict

