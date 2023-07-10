import base64
import hashlib
import hmac
import json

def remove_padding(encoded_string):
    return encoded_string.rstrip("=")


def jwt_creator(secret_key):
        encoded_header = 'eyJhbGciOiJNRDVfSE1BQyJ9'
        encoded_payload = 'eyJ1c2VybmFtZSI6InMifQ'

        encoded_token = encoded_header + "." + encoded_payload

        signature = hmac.new(secret_key.encode("utf-8"), encoded_token.encode("utf-8"), hashlib.md5).digest()
        encoded_signature = remove_padding(base64.urlsafe_b64encode(signature).decode("utf-8"))

        jwt_token = encoded_token + "." + encoded_signature

        return jwt_token

or_jwt = 'eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6InMifQ.49BQc1Pj96LW8tUhAHXzYA'

permutations_file = 'permutations.txt'
secret_found = None

with open(permutations_file, 'r') as f:
    for line in f:
        secret_key = line.strip()
        token = jwt_creator(secret_key)
        print(token)
        if token == or_jwt:
            secret_found = secret_key
            break

if secret_found:
    print("Found secret: " + secret_found)
else:
    print("No matching secret found.")