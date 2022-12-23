#  Install the Python Requests library:
# `pip install requests`
import requests

def send_request():
    response = requests.post(
        url='https://app.scrapingbee.com/api/v1?project_id=86025&competition_id=125&specialism_id=9',
        params={
            'api_key': 'OLVGWN0E9V8I16WV23QPJ2TA6AY8UTDF7ERRBZ95O84LHQO5OBNVIDY2XXIUI2EKSZCDO12LORJCSDIR',
            'url': 'https://artsthread.com/wp-json/artsthread/v1/app-vote', 
            'render_js': 'true',
            'forward_headers': 'true', 
        },
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
    )
    print('Response HTTP Status Code: ', response.status_code)
    print('Response HTTP Response Body: ', response.text)
send_request()