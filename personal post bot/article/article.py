import requests
from requests.structures import CaseInsensitiveDict
import json
from stem import Signal
from stem.control import Controller


def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {
        "http": "socks5://127.0.0.1:9050",
        "https": "socks5://127.0.0.1:9050",
    }
    return session


def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="keyaan786")
        controller.signal(Signal.NEWNYM)


url = "https://smodin.io/smodin-service/write"

headers = CaseInsensitiveDict()
headers["authority"] = "smodin.io"
headers["accept"] = "application/json, text/plain, */*"
headers["accept-language"] = "en-US,en;q=0.9"
# headers["authorization"] = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImVhNWY2NDYxMjA4Y2ZmMGVlYzgwZDFkYmI1MjgyZTkyMDY0MjAyNWEiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiS2V5YWFuIE1pbmhhcyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQUZkWnVjcE9UZkdhbHVaeWlHOFIwUXVRTmpyb0dhTDFxZlBhUFdpY0pfUVAwdz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9zbW9kaW4tcHJvZCIsImF1ZCI6InNtb2Rpbi1wcm9kIiwiYXV0aF90aW1lIjoxNjU3NTgwMDMwLCJ1c2VyX2lkIjoidVp3dHZ1ZlhjSWV2NFJIRTlXTE14T3U4aUdwMSIsInN1YiI6InVad3R2dWZYY0lldjRSSEU5V0xNeE91OGlHcDEiLCJpYXQiOjE2NTc5OTg1NDgsImV4cCI6MTY1ODAwMjE0OCwiZW1haWwiOiJrZXlhYW5taW5oYXNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMDk3MDM5Mzk2MTUxNDkwNjY4MzUiXSwiZW1haWwiOlsia2V5YWFubWluaGFzQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.mu7RcrYTSZ3vgT8u22rnjD7wBxY3DlVxTps2LaiO2RkJ74wBk0WmMN1qVXhqx3kUxsekFcpJectAW7owEENIcjeIKfa9FlvfxD3sFjMXadRlx1f9-J_gW4so8gtVT0JO3iaIOJcWYw880GqMvNeweg2B7NCHpQOp7W1TX3zXi4_7BlZ-xc2kaf9dtDoxm3TO4qlCuM6WZrAd84Hf06XmGvPAovSG9j5L0HlLbQtCxHZt4g4eRQ4koLsCCm2F6AdGHSvJPzQqNPKJ1zKcVyLkbDZdwrKqgan4XbQPiJO6Lkd0eHNbkkOIpzpmxjedc_JZ27PtfXgFSbchCNSPaT7UfQ"
headers["content-type"] = "application/json;charset=UTF-8"
# headers["cookie"] = "_fbp=fb.1.1657579798714.1468343778; _tt_enable_cookie=1; _ttp=dfb9096d-c39f-488e-8a30-daffdb4ce7d3; __gads=ID=4fb8b776854dc4fd-2202d84d47d40056:T=1657579800:RT=1657579800:S=ALNI_MYURk4eGbew8-BxYJhbEF_W8ZJqAA; _gid=GA1.2.1821065780.1657998554; __gpi=UID=000009e13081b6f9:T=1657579800:RT=1657998556:S=ALNI_MZ-UdyNylzWg6hVK6yhbeJB6ywjsg; _gat_gtag_UA_119340507_5=1; _ga_0W23F1LBQH=GS1.1.1657998548.4.1.1657998697.43; _ga=GA1.1.758720536.1657579799"
headers["origin"] = "https://smodin.io"
headers["referer"] = "https://smodin.io/writer"
headers["sec-ch-ua"] = "Not;A Brand"
v = "99", "Microsoft Edge"
v = "103", "Chromium"
v = "103"
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = "Windows"
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "same-origin"
# headers["x-json-ip"] = "115.186.9.140"


with open("titles.txt", "r") as d:
    questions = d.readlines()

for question in questions:
    question = question.strip()
    data = (
        '{"prompt":"'
        + question
        + '","language":"en","writingType":"article","paragraphCount":6,"articleType":"outline","detectLang":false}'
    )
    print(question)
    count = 0
    while count != -1:
        try:
            session = get_tor_session()
            renew_connection()
            resp = session.post(url, headers=headers, data=data)
            data = resp.json()
            break
        except Exception as e:
            count += 1
            print(count, e)
            pass
    # data = json.loads(lol)
    final = ""
    all_chars = (
        " abcdefghijklmnopqrstuvwxyz,.:!?/()*1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    title = data["title"]
    paragraphs = data["paragraphs"]
    with open(f"ALL_TITLES/{question.strip()}.txt", "a") as f:
        for para in paragraphs:
            x = para["text"]
            f.write(x + "\n")
    with open("done.txt", "r") as f:
        done_lines = f.readlines()
    with open("titles.txt", "r") as b:
        not_done_lines = b.readlines()
    with open("titles.txt", "w") as d:
        for notdone in not_done_lines:
            if notdone not in done_lines:
                d.write(notdone)
