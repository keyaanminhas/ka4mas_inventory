
from bs4 import BeautifulSoup
from lxml import etree
import requests
cookies = {
    'referral_params': 'dfss22',
    'flaid': '4daac9ca-5ded-46e4-a37f-b8671b8d0cd6',
    'SID': '55b77d1474d211d7b132b8348af0de00',
    '_gcl_au': '1.1.1741541306.1658946194',
    'ac_enable_tracking': '1',
    '_ga_20X69CEG73': 'GS1.1.1658946196.1.0.1658946196.0',
    '_uetsid': '2eb997200dd911ed90cd31f281a709df',
    '_uetvid': '2eb9b6800dd911eda3944fc63431c7ac',
    '_ga': 'GA1.2.1206096499.1658946196',
    '_gid': 'GA1.2.1532238920.1658946196',
    '_gat_UA-8798837-11': '1',
    'mp_dabc4846e23100ec2d82c44df7430fac_mixpanel': '%7B%22distinct_id%22%3A%20%2218240e6137cd48-06c8a0c2e76e17-76492e29-16e360-18240e6137deb8%22%2C%22%24device_id%22%3A%20%2218240e6137cd48-06c8a0c2e76e17-76492e29-16e360-18240e6137deb8%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%22%24os%22%3A%20%22Windows%22%2C%22%24browser%22%3A%20%22Microsoft%20Edge%22%2C%22%24browser_version%22%3A%20103%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    '_fbp': 'fb.1.1658946196553.271967343',
    '_hjSessionUser_1295979': 'eyJpZCI6IjkyMWJhNTgxLWNlNzItNWUxYy1iYzgxLTk3OGMwYmRhYjRmNyIsImNyZWF0ZWQiOjE2NTg5NDYxOTY2ODUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjSession_1295979': 'eyJpZCI6IjFhNzgzYTZiLTdjOGQtNDkwNS04ZjI5LThjNTVlMTYwMjc2NiIsImNyZWF0ZWQiOjE2NTg5NDYxOTY2OTYsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
    '_hjCachedUserAttributes': 'eyJhdHRyaWJ1dGVzIjp7fSwidXNlcklkIjpudWxsfQ==',
    '_hjIncludedInSessionSample': '0',
    'MTXTRACK_ID': '115.186.9.200%3A71c7493362054e86e1d9724907bb95cf',
    'MTXVISITOR_ID': '3b8e222d3a0eafc87b7191e5ed861116',
    'MTXFIRSTTIME_VST': '1658947460081',
    'outbrain_cid_fetch': 'true',
    '_clck': '16mjc0b|1|f3i|0',
    '_aimtellSubscriberID': 'b0a26102-c12f-6e3c-635b-9915ce67ada3',
    '__hstc': '6238636.c4eab839533e8045241f4649c07fd615.1658946198309.1658946198309.1658946198309.1',
    'hubspotutk': 'c4eab839533e8045241f4649c07fd615',
    '__hssrc': '1',
    '__hssc': '6238636.1.1658946198309',
    '_clsk': '79ovz3|1658946198459|1|1|i.clarity.ms/collect',
    '__ssid': '7117e157143d5d22f36db7aeeec3014',
}

headers = {
    'authority': 'flippa.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'referral_params=dfss22; flaid=4daac9ca-5ded-46e4-a37f-b8671b8d0cd6; SID=55b77d1474d211d7b132b8348af0de00; _gcl_au=1.1.1741541306.1658946194; ac_enable_tracking=1; _ga_20X69CEG73=GS1.1.1658946196.1.0.1658946196.0; _uetsid=2eb997200dd911ed90cd31f281a709df; _uetvid=2eb9b6800dd911eda3944fc63431c7ac; _ga=GA1.2.1206096499.1658946196; _gid=GA1.2.1532238920.1658946196; _gat_UA-8798837-11=1; mp_dabc4846e23100ec2d82c44df7430fac_mixpanel=%7B%22distinct_id%22%3A%20%2218240e6137cd48-06c8a0c2e76e17-76492e29-16e360-18240e6137deb8%22%2C%22%24device_id%22%3A%20%2218240e6137cd48-06c8a0c2e76e17-76492e29-16e360-18240e6137deb8%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%22%24os%22%3A%20%22Windows%22%2C%22%24browser%22%3A%20%22Microsoft%20Edge%22%2C%22%24browser_version%22%3A%20103%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _fbp=fb.1.1658946196553.271967343; _hjSessionUser_1295979=eyJpZCI6IjkyMWJhNTgxLWNlNzItNWUxYy1iYzgxLTk3OGMwYmRhYjRmNyIsImNyZWF0ZWQiOjE2NTg5NDYxOTY2ODUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_1295979=eyJpZCI6IjFhNzgzYTZiLTdjOGQtNDkwNS04ZjI5LThjNTVlMTYwMjc2NiIsImNyZWF0ZWQiOjE2NTg5NDYxOTY2OTYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7fSwidXNlcklkIjpudWxsfQ==; _hjIncludedInSessionSample=0; MTXTRACK_ID=115.186.9.200%3A71c7493362054e86e1d9724907bb95cf; MTXVISITOR_ID=3b8e222d3a0eafc87b7191e5ed861116; MTXFIRSTTIME_VST=1658947460081; outbrain_cid_fetch=true; _clck=16mjc0b|1|f3i|0; _aimtellSubscriberID=b0a26102-c12f-6e3c-635b-9915ce67ada3; __hstc=6238636.c4eab839533e8045241f4649c07fd615.1658946198309.1658946198309.1658946198309.1; hubspotutk=c4eab839533e8045241f4649c07fd615; __hssrc=1; __hssc=6238636.1.1658946198309; _clsk=79ovz3|1658946198459|1|1|i.clarity.ms/collect; __ssid=7117e157143d5d22f36db7aeeec3014',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
}

params = {
    'buy_sell': 'dfss22',
    'sort_alias': 'most_active',
    'search_template': 'most_relevant',
    'filter[site_type_tag]': 'adsense',
    'filter[sale_method]': 'auction',
}

response = requests.get('https://flippa.com/buy/monetization/adsense', params=params, cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

print(soup)

# dom = etree.HTML(str(soup))

# print(dom.xpath('/html/body/div[3]/div[3]/form/div/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[1]/a[2]/div/div[1]')[0].text)
