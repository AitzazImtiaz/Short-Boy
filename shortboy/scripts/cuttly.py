import requests
import time
from colorama import Fore
import os
os.system("clear")

import requests

api_key = "64d1303e4ba02f1ebba4699bc871413f0510a"
# the URL you want to shorten
url = input("Enter your url:")

# preferred name in the URL
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
# or
# api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"
# make the request
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)
n = input("Enter y to return:")
if n=="y":
  os.system("python shortboy/__main__.py")
