import requests

url  = 'https://webhacking.kr/challenge/bonus-8/index.php.swp'
r = requests.get(url, allow_redirect=True)
open('index.swp', "wb").write(r.content)