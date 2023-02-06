import json

import requests

url = f"https://kun.uz/news/list"
resp = requests.get(url, params={"f": "actual"})

print(resp.text)
