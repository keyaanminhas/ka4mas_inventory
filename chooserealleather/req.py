
import requests
from time import sleep
import random

import urllib.request as urlrequest
import urllib.parse
from requests_toolbelt.utils import dump



def get_session(poxy):
    session = requests.Session()
    session.proxies = {"http://": proxy, "https://": proxy}
    return session, proxy


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://chooserealleather.com',
    'Referer': 'https://chooserealleather.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'project_id': '86025',
    'competition_id': '125',
    'specialism_id': '9',
}


with open('config.txt', 'r') as f:
    conf = f.readlines()
    tipe = conf[0].strip()
    filetoopen = conf[1].strip()
    timerange = conf[2].strip()
    time1, time2 = timerange.split(',')


with open(f'{filetoopen}', 'r') as f:
    n = f.readlines()
    x = [z.split() for z in n]


count = 1
while count < len(x):
    poxy = x[count]
    poxy = poxy[0]

    print(poxy)
    if tipe == 'socks5':
        proxies = {
            "http":f"socks5://{poxy}",
            "https":f"socks5://{poxy}"
        }
    elif tipe == 'socks4':
        proxies = {
            "http":f"socks4://{poxy}",
            "https":f"socks4://{poxy}"
        }
    elif tipe == 'https' or tipe == 'http':
        proxies = {
            "http":f"{poxy}",
            "https":f"{poxy}"
        }
    else:
        print('Please specify the type of proxies')

    try:
        session = requests.Session()
        session.proxies = proxies
        response = session.post('https://artsthread.com/wp-json/artsthread/v1/app-vote', headers=headers, data=data, timeout = 10)
        print(dump.dump_all(response).decode("utf-8"))
        print('VOTE ADDED')
        sleep(random.randint(int(time1)* 60, int(time2) * 60))
    
    except Exception as e:
        print("PROXY FAILED")

    count = count + 1






























