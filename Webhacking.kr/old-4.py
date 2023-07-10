import hashlib
import requests
def hash(num):
    m  = f'{num}salt_for_you'
    for _ in range(500):
        m = hashlib.sha1(m.encode('utf-8')).hexdigest()
    return m
url = 'https://webhacking.kr/challenge/web-04'
for num in range(10000000, 99999999):
    r = requests.post(url, data = {
        "PHPSESSID": "ivpign46edq5u1fmkvjsj6q3n2",
        "key" : hash(num)})
    if r.text == "solved":
        exit()