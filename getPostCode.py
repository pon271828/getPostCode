import requests
import sys
import json

args = sys.argv

url = "https://zipcloud.ibsnet.co.jp/api/search"

pyaload = {"zipcode" : args[1]}

r = requests.get(url, pyaload)

with  open("response.json", "w") as f:
    json.dump(r.json(), f, indent = 2, ensure_ascii = False)

print(json.dumps(r.json(), indent=2, ensure_ascii=False))
