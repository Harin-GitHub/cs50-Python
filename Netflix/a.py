import requests
import json

response = requests.get(
    "https://api.spotify.com/v1/recommendations/available-genre-seeds"
)
print(json.dumps(response.json(), indent=2))
