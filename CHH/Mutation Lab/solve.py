import hmac
from hashlib import sha1
import base64
key = 'ngz7aqqvfnrc4V3BfjsXyHUk21B48PnD'
msg = 'session=eyJ1c2VybmFtZSI6ImFkbWluIn0'
session = base64.b64encode(b'{"username":"admin"}')
sig = hmac.digest(key.encode(), msg.encode(), sha1)
print(base64.urlsafe_b64encode(sig))

print(session)
