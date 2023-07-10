import random
from base64 import b64encode, b64decode
import hashlib
import json


data_cookie = 'eyJ1c2VybmFtZSI6ICJuZ29jIiwgInVzZXJfdHlwZSI6ICJiYXNpYyJ9'
hash_cookie = '8529e1f31c3682725b54d02c3a07b5582bea7844624d3804aa813db2a52931bb'
username = 'ngoc'

def hash(data):
    return hashlib.sha256(bytes(data, 'utf-8')).hexdigest()
def crack():
    
    data = {
        "username": username,
        "user_type":"basic"
    }
    for i in range(0xFFFFFF):
        r = hex(i)[2:]
        b64data = b64encode(json.dumps(data).encode())
        data_hash = hash(b64data.decode() + r) 
        if b64data.decode() == data_cookie and data_hash == hash_cookie:
            return r
        i += 1
        if i % 1000000 == 0:
            print(f"{i=}")   
def force(r):
    data = {"username": username, "user_type":"premium"}
    
    b64data = b64encode(json.dumps(data).encode())
    data_hash = hash(b64data.decode() + r)
    
    print(f"{b64data=} {data_hash=}")
    
    
if __name__ == "__main__":
    # print(crack())
    r = "9fba4d"
    force(r)