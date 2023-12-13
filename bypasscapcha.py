import requests

r = requests.get("")

def find_between(s, start, end):
    return (s.split(start)[1]).split(end)[0]
c_string  = find_between(r.text, "name=\"c\" value=\"", "\">")
