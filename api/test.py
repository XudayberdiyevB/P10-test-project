import json

import requests

KEY = "gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR"

# Method 1
# url = f"https://api.freecurrencyapi.com/v1/latest?apikey={KEY}"
# resp = requests.get(url)

# Method2
url = f"https://api.freecurrencyapi.com/v1/latest"
resp = requests.get(
    url,
    params={"apikey": KEY}
)

print(resp.text)

with open("weather.json", "w") as f:
    json.dump(json.loads(resp.text), f)
