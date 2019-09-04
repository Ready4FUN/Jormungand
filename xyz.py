import requests
import json

url = "https://xyz.api.here.com/hub/spaces/YlAje4LF/features/"

data = {
    "type": "Feature",
    "id": "BfiimUxHjj",
    "geometry": {
        "type": "Point",
        "coordinates": [
            37.4541567,
            55.8807606 
        ]
    },
    "properties": {
        "Temperature": 25,
        "Humidity": 55,
        "co2": 500
    }
  }

payload = json.dumps(data)

headers = {"Authorization": "Bearer AHBXmO0MIhGyWKZVH26Indo", "Content-Type": "application/geo+json"}

r = requests.put(url, data=payload, headers=headers)

print(r.status_code)
print(r.content)