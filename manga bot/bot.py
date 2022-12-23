
#IMPORTS
from discord.ext import tasks
import discord   #Discord Library
from discord.ext import commands #Extensions from discord.ext
from discord.ext.commands import has_permissions, CheckFailure #Importing functions directly
import chromedriver_autoinstaller
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import random
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup

blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


#DISCORD BOT BASIC INITIALIZATION

intents = discord.Intents.all()
intents.members = True #To access members information

client = commands.Bot(intents=intents,command_prefix = "!") #MAIN CLIENT USED TO COMUNICATE WITH DISCORD

client.remove_command('help') #To create our own help command which is better than Default one :)

client.intents.members = True #To make sure Member information is accessible



#BEGINNING OF CODE
@tasks.loop(seconds = 6)
async def here(ctx, word):
	message = ''
	output = ''
	embed = discord.Embed(
		colour = discord.Color.random()
	)

	with open('links.txt','r') as handle:
		links = handle.readlines()
	for link in links:
		res = requests.get(link, headers = headers)
		htm = res.content
		soup = BeautifulSoup(htm, 'html.parser')
		for t in soup:
			output += '{} '.format(t)
		if output.find(word) != -1:
			message = message + f'\n WORD: {word}'+ '\n'+  f' LINK: {link} FOUND!!!' + '\n'*2
		else:
			message = message + f' \n WORD: {word}'+ '\n'+  f' LINK: {link} NOT FOUND!!!' + '\n'*2
	embed.add_field(name = 'CHECKING WORD', value = message)
	await ctx.channel.send(embed = embed)

    



@client.event #Discord library's predefined-function which waits for activity
async def on_ready(): #When the bot becomes ready
	print("BOT IS STARTED") #Awares us that its started
	await client.change_presence(activity=discord.Game(name="Stock Monitor")) #Presence or activity which makes it look cool



#HELP COMMAND

@client.command(aliases=[' help']) #Different key words to be considered the same
async def help(ctx): #defining the function
	embed = discord.Embed(
		colour = discord.Color.random()
	) # Embed are a way to represent information on discord

	embed.set_author(name ='HELP')# Title of message
	#CONTENT OF MESSAGE
	embed.add_field(name = '!help', value = 'SHOWS THIS COMMAND', inline=False)
	embed.add_field(name = '!add <link>', value = 'ADDS THE LINK', inline = False)
	embed.add_field(name = '!check <word>', value = 'CHECK A WORD ON THE LINKS', inline = False)
	embed.add_field(name = '!list', value = 'LIST ALL THE LINKS', inline = False)
	await ctx.author.send(embed=embed) #SENDING THE MESSAGE ON DISCORD




#DASHBOARD COMMAND
@client.command(aliases=[' add'])
async def add(ctx, * ,link):
	embed = discord.Embed(
		colour = discord.Color.random()
	)

	try:
		with open('links.txt', 'a') as f:
			f.write(link + '\n' )
		await ctx.channel.send(f'ADDED {link}')

	except:
		await ctx.channel.send('UNKNOWN ERROR')




@client.command(aliases=[' list'])
async def list(ctx):
	message = ''
	embed = discord.Embed(
		colour = discord.Color.random()
	)
	with open('links.txt','r') as handle:
		links = handle.readlines()
	for link in links:
		message = message + link + '\n'*2

	try:

		embed.add_field(name = 'ALL THE LINKS', value = message)
		await ctx.channel.send(embed = embed)
	except:
		await ctx.channel.send('NO LIST')


@client.command(aliases = [' start'])
async def start(ctx, *, word):
	here.start(ctx, word)

@client.command(aliases = [' stop'])
async def stop(ctx):
	here.stop()

@client.command(aliases = [' check'])
async def check(ctx,* , word):
	message = ''
	embed = discord.Embed(
		colour = discord.Color.random()
	)

	with open('links.txt','r') as handle:
		links = handle.readlines()
	for link in links:
		res = requests.get(url, headers = headers)
		html_page = res.content
		if html_page.find(word) != -1:
			message = message + f'\n WORD: {word}'+ '\n'+  f' LINK: {link} FOUND!!!' + '\n'*2
		else:
			message = message + f' \n WORD: {word}'+ '\n'+  f' LINK: {link} NOT FOUND!!!' + '\n'*2
	embed.add_field(name = 'CHECKING WORD', value = message)
	await ctx.channel.send(embed = embed)





@client.command(aliases=[' clean', 'clean', ' clear'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit = amount + 1)

token = 'OTE4ODA4ODA3Mzc3ODYyNjk2.YbMpYg.uYKqpy9h93eUd3BhVhT4uU_Kvm0'

client.run(token)






