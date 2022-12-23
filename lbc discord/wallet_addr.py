import json
import hmac
import time
import hashlib
import requests


hmac_key = '74a2e6f8ec4efee4650b30c498c27870'
hmac_secret = 'c92be700281ad7ed519140e9517bd1865a2a89ab5ffe7fffbcdecdcb2e68a36e'

nonce = int(time.time())
api_endpoint ="/api/wallet-addr/"
url = "https://localbitcoins.com/api/wallet-addr/"
get_or_post_params_urlencoded = ""
message = str(nonce) + hmac_key + api_endpoint + get_or_post_params_urlencoded
message_bytes = message.encode('utf-8')
signature = hmac.new(hmac_secret.encode('utf-8'), msg=message_bytes, digestmod=hashlib.sha256).hexdigest().upper()

resp = requests.post(url, headers = {'Apiauth-Key': hmac_key,
	'Apiauth-Nonce': str(nonce),
	'Apiauth-Signature': signature})

data = resp.json()
data = data['data']
unused_address = data['address']

print(unused_address)