import hashlib
from itertools import chain

probably_public_bits = [
	'web-app', # username
	'flask.app',# modname 고정
	'Flask',    # getattr(app, '__name__', getattr(app.__class__, '__name__')) 고정
	'/usr/local/lib/python3.11/site-packages/flask/app.py' # getattr(mod, '__file__', None),
                                                          # python 버전 마다 위치 다름
]
 
private_bits = [
	'2485377892376',  # MAC주소를 int형으로 변환한 값,  
	b'53dbb5ec-74bb-4bc0-9ef6-7c65e87d1270user@1045.service'   # get_machine_id()
]
 
h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
	if not bit:
		continue
	if isinstance(bit, str):
		bit = bit.encode('utf-8')
	h.update(bit)
h.update(b'cookiesalt')
#h.update(b'shittysalt')
 
cookie_name = '__wzd' + h.hexdigest()[:20]
 
num = None
if num is None:
	h.update(b'pinsalt')
	num = ('%09d' % int(h.hexdigest(), 16))[:9]
 
rv =None
if rv is None:
	for group_size in 5, 4, 3:
		if len(num) % group_size == 0:
			rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
						  for x in range(0, len(num), group_size))
			break
	else:
		rv = num
 
print(rv)