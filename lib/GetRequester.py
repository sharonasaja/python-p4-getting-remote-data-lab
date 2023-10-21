import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
         try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
            return response.text
         except requests.exceptions.RequestException as e:
            # Handle any request exceptions (e.g., connection error, timeout)
          print(f"An error occurred: {e}")
          return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body is not None:
            try:
                data = json.loads(response_body)
                return data
            except json.JSONDecodeError as e:
                print(f"Failed to decode JSON: {e}")
                return None
        else:
            return None

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)

response_body = requester.get_response_body()
if response_body:
    print("Response Body:")
    print(response_body)

json_data = requester.load_json()
if json_data:
    print("JSON Data:")
    print(json_data)
