import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions, CheckFailure
import random
import requests
import asyncio
import json
import hmac
import time
import hashlib


hmac_key = '74a2e6f8ec4efee4650b30c498c27870'
hmac_secret = 'c92be700281ad7ed519140e9517bd1865a2a89ab5ffe7fffbcdecdcb2e68a36e'

nonce = int(time.time())
api_endpoint ="/api/wallet/"
url = "https://localbitcoins.com/api/wallet/"
get_or_post_params_urlencoded = ""
message = str(nonce) + hmac_key + api_endpoint + get_or_post_params_urlencoded
message_bytes = message.encode('utf-8')
signature = hmac.new(hmac_secret.encode('utf-8'), msg=message_bytes, digestmod=hashlib.sha256).hexdigest().upper()

resp = requests.get(url, headers = {'Apiauth-Key': hmac_key,
	'Apiauth-Nonce': str(nonce),
	'Apiauth-Signature': signature})

data = resp.json()


data = data['data']

message = data['message']
print(message)

total = data['total']
balance = total['balance']
sendable = total['sendable']
print(balance, sendable)

recieving_addr = data['receiving_address']
print(recieving_addr)

old_addrs = data['old_address_list']
for addrs in old_addrs:
	address = addrs['address']
	recieved = addrs['received']
	print('\n'*3, address, recieved)

received_transactions = data['received_transactions_30d']
for recv_trans in received_transactions:
	txid = recv_trans['txid']
	amount = recv_trans['amount']
	created_at = recv_trans['created_at']
	description = recv_trans['description']
	tx_type = recv_trans['tx_type']
	print('\n'*2, txid, amount, created_at, description, tx_type)

	sent_transactions = data['received_transactions_30d']
for sent in sent_transactions:
	txid = sent['txid']
	amount = sent['amount']
	created_at = sent['created_at']
	description = sent['description']
	tx_type = sent['tx_type']
	print('\n'*2, txid, amount, created_at, description, tx_type)