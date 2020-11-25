#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

from requests import get

ip = get('https://api.ipify.org').text
print('{}'.format(ip))
print("---")
print("ipinfo.io" + " | href=""https://ipinfo.io/")
print("ipleak.net" + " | href=""https://ipleak.net")
