
#IMPORTS

import discord   #Discord Library
from discord.ext import commands #Extensions from discord.ext
from discord.ext.commands import has_permissions, CheckFailure #Importing functions directly
import hmac #Hmac is used for hashing and authentication process
import time #Used to later generate a unique number greater than the last
import hashlib #To hash
import requests #To call api or send requests to api
import os #To get environment variables
from dotenv import load_dotenv #To load .env file
import json #To parse json data



load_dotenv() #Loading the .env file

hmac_key = os.environ.get('hmac_key') #Getting the environment variables 
hmac_secret = os.environ.get('hmac_secret') #hmac secret later used for signatures
TOKEN = os.environ.get('token') #Discord BOT Token



#DISCORD BOT BASIC INITIALIZATION

intents = discord.Intents.all()
intents.members = True #To access members information

client = commands.Bot(intents=intents,command_prefix = "//") #MAIN CLIENT USED TO COMUNICATE WITH DISCORD

client.remove_command('help') #To create our own help command which is better than Default one :)

client.intents.members = True #To make sure Member information is accessible



#BEGINNING OF CODE

@client.event #Discord library's predefined-function which waits for activity
async def on_ready(): #When the bot becomes ready
	print("BOT IS STARTED") #Awares us that its started
	await client.change_presence(activity=discord.Game(name="CryptoBot")) #Presence or activity which makes it look cool



#HELP COMMAND

@client.command(aliases=[' help']) #Different key words to be considered the same
@commands.has_permissions(administrator=True) #Check if the user has administrator permission
async def help(ctx): #defining the function
	embed = discord.Embed(
		colour = discord.Color.random()
	) # Embed are a way to represent information on discord

	embed.set_author(name ='HELP')# Title of message
	#CONTENT OF MESSAGE
	embed.add_field(name = '!help', value = 'SHOWS THIS COMMAND', inline=False)
	embed.add_field(name = '!wallet', value = 'DISPLAYS ALL WALLET INFORMATION', inline = False)
	embed.add_field(name = '!old', value = 'DISPLAYS OLD ADDRESSES WHICH SENT MONEY', inline = False)
	embed.add_field(name = '!recv', value = 'DISPLAYS DETAILS OF RECIEVED TRANSACTIONS', inline = False)
	embed.add_field(name = '!sent', value = 'DISPLAYS DETAILS OF SENT TRANSACTIONS', inline = False)
	embed.add_field(name = '!dashboard', value = 'DISPLAYS THE DASHBOARD', inline = False)
	embed.add_field(name = '!btc <amount>', value = 'DISPLAYS THE DEPOSIT AMOUNT WITH WALLET')
	await ctx.author.send(embed=embed) #SENDING THE MESSAGE ON DISCORD




#DASHBOARD COMMAND
@client.command(aliases=[' dashboard'])
@commands.has_permissions(administrator=True)
async def dashboard(ctx):
	await ctx.channel.purge(limit = 1) #To make the invisible commands or to hide the command
	embed = discord.Embed(
		colour = discord.Color.random()
	)

	nonce = int(time.time()) #Requirement of api for authentication
	api_endpoint ="/api/wallet/" #API endpoint
	url = "https://localbitcoins.com/api/wallet/" #LINK
	get_or_post_params_urlencoded = "" #parameters which we dont need

	#Authentication method mentioned in the documentation
	message = str(nonce) + hmac_key + api_endpoint + get_or_post_params_urlencoded
	message_bytes = message.encode('utf-8')
	signature = hmac.new(hmac_secret.encode('utf-8'), msg=message_bytes, digestmod=hashlib.sha256).hexdigest().upper()
	resp = requests.get(url, headers = {'Apiauth-Key': hmac_key,
	'Apiauth-Nonce': str(nonce),
	'Apiauth-Signature': signature})
	try:
		#COLLECTING DATA FROM THE RESPONSE
		data = resp.json()
		data = data['data']#looks for the key and saves its value
		total = data['total']
		balance = total['balance']
		sendable = total['sendable']
		recieving_addr = data['receiving_address']
		old_addrs = data['old_address_list']
		received_transactions = data['received_transactions_30d']
		sent_transactions = data['sent_transactions_30d']

		embed.set_author(name = 'DASHBOARD')
		embed.add_field(name = 'BALANCE', value = balance, inline = True)
		embed.add_field(name = 'SENDABLE' , value = sendable, inline = True)
		embed.add_field(name = 'RECEIVING_ADDRESS', value = recieving_addr, inline = False)

		await ctx.channel.send(embed=embed)
	except:
		await ctx.channel.send('UNKNOWN ERROR')








@client.command(aliases=[' old'])
@commands.has_permissions(administrator=True)
async def old(ctx):
	await ctx.channel.purge(limit = 1)
	embed = discord.Embed(
		colour = discord.Color.random()
	)

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
	try:
		data = resp.json()
		data = data['data']
		total = data['total']
		balance = total['balance']
		sendable = total['sendable']
		recieving_addr = data['receiving_address']
		old_addrs = data['old_address_list']
		received_transactions = data['received_transactions_30d']
		sent_transactions = data['sent_transactions_30d']
		message = ''

		for addrs in old_addrs:# Looping through all the transactions/data
			address = addrs['address']
			recieved = addrs['received']
			message = message + 'From: '+ address + ' Amount: ' + recieved + '\n'

		embed.add_field(name = 'OLD ADDRESSES', value = message, inline = True)
		await ctx.channel.send(embed=embed)
	except:
		await ctx.channel.send('UNKNOWN ERROR')










@client.command(aliases=[' recv'])
@commands.has_permissions(administrator=True)
async def recv(ctx):
	await ctx.channel.purge(limit = 1)
	embed = discord.Embed(
		colour = discord.Color.random()
	)

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
	try:
		data = resp.json()
		data = data['data']
		total = data['total']
		balance = total['balance']
		sendable = total['sendable']
		recieving_addr = data['receiving_address']
		old_addrs = data['old_address_list']
		received_transactions = data['received_transactions_30d']
		sent_transactions = data['sent_transactions_30d']
		message = ''
		for recv_trans in received_transactions:
			txid = str(recv_trans['txid'])
			amount = str(recv_trans['amount'])
			created_at = str(recv_trans['created_at'])
			description = str(recv_trans['description'])
			tx_type = str(recv_trans['tx_type'])
			#creating the message
			message = message + 'Tx Id: '+ txid+ ' Amount: '+ amount+ ' Created_at: '+ created_at+ ' Description: '+ description + ' Tx type: '+ tx_type + '\n'*2
		
		embed.add_field(name = 'RECEIVED TRANSACTIONS (30d)', value = str(message), inline = True)
		await ctx.channel.send(embed=embed)
	except:
		await ctx.channel.send('UNKNOWN ERROR')







@client.command(aliases=[' sent'])
@commands.has_permissions(administrator=True)
async def sent(ctx):
	await ctx.channel.purge(limit = 1)
	embed = discord.Embed(
		colour = discord.Color.random()
	)

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
	try:
		data = resp.json()
		data = data['data']
		total = data['total']
		balance = total['balance']
		sendable = total['sendable']
		recieving_addr = data['receiving_address']
		old_addrs = data['old_address_list']
		received_transactions = data['received_transactions_30d']
		sent_transactions = data['sent_transactions_30d']
		message = ''
		for sent in sent_transactions:
			txid = str(sent['txid'])
			amount = str(sent['amount'])
			created_at = str(sent['created_at'])
			description = str(sent['description'])
			tx_type = str(sent['tx_type'])
			message = message + 'Tx Id: ' + txid + ' Amount: ' + amount+ ' Created_at: ' + created_at + ' Description: ' + description + ' Tx type: '+ tx_type + '\n'*2 
		embed.add_field(name = 'SENT TRANSACTIONS (30d)', value = message, inline = True)
		await ctx.channel.send(embed=embed)
	except:
		await ctx.channel.send('UNKNOWN ERROR')





#COMMAND TO SEND EVERYTHING (NOT IN USE)

@client.command(aliases=[' all'])
@commands.has_permissions(administrator=True)
async def all(ctx):
	await ctx.channel.purge(limit = 1)
	embed = discord.Embed(
		colour = discord.Color.random()
	)

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
	total = data['total']
	balance = total['balance']
	sendable = total['sendable']
	recieving_addr = data['receiving_address']
	old_addrs = data['old_address_list']
	received_transactions = data['received_transactions_30d']
	sent_transactions = data['sent_transactions_30d']

	embed.set_author(name = 'WALLET')
	embed.add_field(name = 'BALANCE', value = balance, inline = False)
	embed.add_field(name = 'SENDABLE' , value = sendable, inline = False)
	embed.add_field(name = 'RECEIVING_ADDRESS', value = recieving_addr, inline = False)

	for addrs in old_addrs:
		address = addrs['address']
		recieved = addrs['received']
		message = 'From: '+ address + ' Amount: ' + recieved
		embed.add_field(name = 'OLD ADDRESS', value = message, inline = True)

	for recv_trans in received_transactions:
		txid = str(recv_trans['txid'])
		amount = str(recv_trans['amount'])
		created_at = str(recv_trans['created_at'])
		description = str(recv_trans['description'])
		tx_type = str(recv_trans['tx_type'])
		message = 'Tx Id: '+ txid+ ' Amount: '+ amount+ ' Created_at: '+ created_at+ ' Description: '+ description + ' Tx type: '+ tx_type
		embed.add_field(name = 'RECEIVED TRANSACTIONS (30d)', value = str(message), inline = True)
	
	for sent in sent_transactions:
		txid = sent['txid']
		amount = sent['amount']
		created_at = sent['created_at']
		description = sent['description']
		tx_type = sent['tx_type']
		message = 'Tx Id:', txid, 'Amount:', amount, 'Created_at:', created_at, 'Description:', description, 'Tx type:', tx_type
		embed.add_field(name = 'SENT TRANSACTIONS (30d)', value = message, inline = True)
	await ctx.channel.send(embed=embed)



@client.command(aliases=[' wallet'])
@commands.has_permissions(administrator=True)
async def wallet(ctx):
	await ctx.channel.purge(limit = 1)
	embed = discord.Embed(
		colour = discord.Color.random()
	)

	nonce = int(time.time())
	api_endpoint ="/api/wallet-addr/"
	url = "https://localbitcoins.com/api/wallet-addr/"
	get_or_post_params_urlencoded = ""
	message = str(nonce) + hmac_key + api_endpoint + get_or_post_params_urlencoded
	message_bytes = message.encode('utf-8')
	signature = hmac.new(hmac_secret.encode('utf-8'), msg=message_bytes, digestmod=hashlib.sha256).hexdigest().upper()
	resp = requests.get(url, headers = {'Apiauth-Key': hmac_key,
	'Apiauth-Nonce': str(nonce),
	'Apiauth-Signature': signature})
	data = resp.json()
	data = data['data']
	try:
		unused_address = data['address']
		embed.add_field(name = 'WALLET', value=unused_address)
		await ctx.channel.send(embed = embed)
	except:
		await ctx.channel.send('UNKNOWN ERROR')


@client.command(aliases=[' btc'])
@commands.has_permissions(administrator=True)
async def btc(ctx, num):
	await ctx.channel.purge(limit = 1)
	embed = discord.Embed(
		colour = discord.Color.random()
	)

	nonce = int(time.time())
	api_endpoint ="/api/wallet-addr/"
	url = "https://localbitcoins.com/api/wallet-addr/"
	get_or_post_params_urlencoded = ""
	message = str(nonce) + hmac_key + api_endpoint + get_or_post_params_urlencoded
	message_bytes = message.encode('utf-8')
	signature = hmac.new(hmac_secret.encode('utf-8'), msg=message_bytes, digestmod=hashlib.sha256).hexdigest().upper()
	resp = requests.get(url, headers = {'Apiauth-Key': hmac_key,
	'Apiauth-Nonce': str(nonce),
	'Apiauth-Signature': signature})
	try:
		data = resp.json()
		data = data['data']
		unused_address = data['address']
		url = 'https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd'
		res = requests.get(url)
		data = res.json()
		data = data['data']
		data = data[0]
		slug = data['slug']
		symbol = data['symbol']
		metrics = data['metrics']
		market_data = metrics['market_data']
		price_usd = market_data['price_usd']
		url2 = 'https://freecurrencyapi.net/api/v2/latest?apikey=b9c78bf0-55ca-11ec-bd28-fdadc2af85cf'
		resp2 = requests.get(url2)
		data = resp2.json()
		data = data['data']
		gbp = data['GBP']
		total = (float(num)/gbp)/ price_usd #converting stuff
		total = str(total)[0:7] #reducing to 5 decimal places
		embed.set_author(name = "DEPOSIT", icon_url='https://icons.iconarchive.com/icons/pauloruberto/custom-round-yosemite/512/Bitcoin-icon.png')
		message = f'''You are paying the equivalent of £{num} in Bitcoin. 

Please pay {total} + network fees.

BTC wallet: {unused_address}

'''
		embed.add_field(name = 'Amount', value = message + (f"[Track Payment](https://localbitcoinschain.com/address/{unused_address})"), inline=False)
		await ctx.channel.send(embed = embed)
	except:
		await ctx.channel.send('UNKNOWN ERROR')

#TO CLEAR MESSAGES
client.command(aliases=[' clean', 'clean', ' clear'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit = amount + 1)

client.run(TOKEN)






