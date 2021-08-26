import sys
import os
import json
import socket
import requests

sys.path.append(os.getcwd())
sys.path.append('../')
print(sys.path)
from privatekeys.api_keys import apikeys

hostname = socket.gethostname()
ipa = socket.gethostbyname(hostname)
print(hostname + "  " + ipa)

baseurl = "https://ipinfo.io?token="
fullurl = baseurl + apikeys['ipinfo_key']
response = requests.get(fullurl)
x = response.json()
for i in x:
    print(i + " , " + x[i])