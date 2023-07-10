import random
import re

def generate_key():
    key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=17))
    return key

def validate_key(key):
    pattern = r'^[0-9A-Za-z]{3}-[A-Za-z0-9]{4}-[0-9A-Za-z]{6}-[0-9]{2}$'
    if re.match(pattern, key) and sum(ord(char) for char in key) % 7 == 0:
        return True
    return False

# Generate a valid key
while True:
    key = generate_key()
    if validate_key(key):
        print(f"Valid key: {key}")
        break
