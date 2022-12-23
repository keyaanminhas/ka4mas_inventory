f = open('tokens.txt', 'w')

import requests
https_proxy = 'https://54.157.145.149:49205'
proxyDict = { 
              "https" : https_proxy
            }

link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v9/invite/" + str(link)

token = "NjkzNTMzNTczMTA1NDUxMDg5.YUt9Hw.ROGwuPMZjK0rO1R4Jqs6IS-tj8E"

headers = {
    'Host': 'discord.com',
    'Content-Length': '2',
    'Authorization': token,
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Connection': 'close',
}

data = '{}'

response = requests.post(apilink, headers=headers, data=data, verify=False)

