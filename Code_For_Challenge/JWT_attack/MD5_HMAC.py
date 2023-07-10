import base64
import json
import hashlib
import hmac

header = {
    "alg": "MD5_HMAC"
}
payload = {
    "username": "admin"
}

token = base64.urlsafe_b64encode(bytearray(json.dumps(header), "utf-8")).rstrip(b"=") + b"."\
        + base64.urlsafe_b64encode(bytearray(json.dumps(payload), "utf-8")).rstrip(b"=")

hmac_md5 = hmac.new(bytes("fsrwjcfszegvsyfa", "utf-8"), token, hashlib.md5)

token = token + b"." + base64.urlsafe_b64encode(hmac_md5.digest())

print(token.decode("utf-8"))