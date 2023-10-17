import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"
endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/"

response = requests.get(endpoint)
print(response.text)
