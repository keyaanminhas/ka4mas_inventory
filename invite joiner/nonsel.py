import requests
from time import sleep
import random
invite_url = input("Enter a Discord invite URL: ")
sleeptime = int(input("Please Enter The Sleep Time In Seconds: "))
invite_code = invite_url.split("/")[-1]

with open('proxies.txt', 'r') as proxies:
    proxylist = proxies.readlines()

api_url = "https://discord.com/api/v9/invites/" + invite_code
with open('tokens.txt','r') as tokenraw:
        tokens = tokenraw.readlines()
        for x in tokens:
            prox = proxylist[random.randint(0,len(proxylist)-1)]
            username = prox.split(":")[-2]
            password = prox.split(":")[-1]
            port = prox.split(":")[-3]
            ip = prox.split(":")[0]
            final_proxy = 'http://' + username + '@' + password + ':' + ip + ':' + port
            proxys = {
                "http": final_proxy
                }
            token = x.rstrip()
            resp = requests.post(api_url, headers={"Authorization": token}, proxies = proxys)

            if resp.ok:
                print(token, "HAS JOINED THE SERVER")
            sleep(sleeptime)

print("Script Complete")
