import requests
import time
from colorama import Fore
import os
os.system("clear")
# account credentials
username = "stupidchills4u"
password = "uselessvibes123!"

print("If this doesn't work, try Cuttly, it will always work.")
time.sleep(3)
# get the access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    # if response is OK, get the access token
    access_token = auth_res.content.decode()
    print("[!] Got access token:", access_token)
else:
    print("[!] Cannot get access token, exiting...")
    exit()
# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()
# the URL you want to shorten
url = input(Fore.MAGENTA+"Enter your URL:")
# make the POST request to get shortened URL for `url`
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    # if response is OK, get the shortened URL
    link = shorten_res.json().get("link")
    print("Shortened URL:", link)
n = input("Enter y to return:")
if n=="y":
  os.system("python shortboy/__main__.py")
