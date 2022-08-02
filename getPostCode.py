import requests
import sys
import json

args = sys.argv

url = "https://zipcloud.ibsnet.co.jp/api/search"

payload = {"zipcode" : args[1]}

r = requests.get(url, params=payload)

r_json = r.json()

with open("response.json", "w") as f:
    json.dump(r_json, f, indent = 2, ensure_ascii = False)

if r_json.get("status") == 400:
    print("入力エラー")
elif r_json.get("status") == 500:
    print("利用しているAPIでエラーが発生しました。")
elif r_json.get("results") == None:
    print("その郵便番号に対応する住所は存在しません。")
else:
    with open("response.txt", "w") as f:
        for r_json_result in r_json.get("results"):

            address = r_json_result.get("address1")+ r_json_result.get("address2") + r_json_result.get("address3")

            print(address)

            f.write(address + "\n")

    

