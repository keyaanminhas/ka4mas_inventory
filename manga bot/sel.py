
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
from google_trans_new import google_translator


translator = google_translator()
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



opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

#BEGINNING OF CODE
@tasks.loop(seconds = 10)
async def here(ctx):
	message = ''
	output = ''

	embed = discord.Embed(
		colour = discord.Color.random()
	)


	with open('links.txt','r') as handle:
		links = handle.readlines()
	for link in links:
		run,link, word = link.split(' ', 2)
		if run == 'run=1':
			linked = f'https://translate.google.com/translate?sl=auto&tl=en&u={link}'
			driver.get(linked)
			output = driver.page_source
			body = driver.find_element_by_tag_name('body')
			text = body.text
			text = text.lower()
			print(text)
			if text.find(word) != -1:
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
	embed.add_field(name = '!add <link> <word_to_find>', value = 'ADDS THE LINK', inline = False)
	embed.add_field(name = '!remove <id_of_link>', value = 'REMOVES THE LINK ON THAT SPOT', inline= False)
	embed.add_field(name = '!set <id_of_link> <true or false>', value = 'TO SET THE RUN STATUS TO TRUE OR FALSE', inline= False)
	embed.add_field(name = '!word <id_of_link> <WORD>', value = 'CHANGES THE WORD WHICH IS SEARCHED', inline= False)
	embed.add_field(name = '!start', value = 'STARTS SEARCHING THE WEBSITES', inline= False)
	embed.add_field(name = '!stop', value = 'STOPS SEARCHING THE WEBSITES', inline= False)
	embed.add_field(name = '!settings', value = 'LIST ALL THE LINKS', inline = False)
	await ctx.channel.send(embed=embed) #SENDING THE MESSAGE ON DISCORD




#DASHBOARD COMMAND
@client.command(aliases=[' add'])
async def add(ctx, * ,link):
	embed = discord.Embed(
		colour = discord.Color.random()
	)

	try:
		with open('links.txt', 'a') as f:
			f.write('run=1 ' + link + '\n' )
		await ctx.channel.send(f'ADDED {link}')

	except:
		await ctx.channel.send('UNKNOWN ERROR')




@client.command(aliases=[' settings', ' setting', 'list'])
async def settings(ctx):
	message = ''
	embed = discord.Embed(
		colour = discord.Color.random()
	)
	with open('links.txt','r') as handle:
		links = handle.readlines()
	i= 0
	for link in links:
		i = i + 1
		message = message + f'[{i}] ' +link + '\n'*2

	try:

		embed.add_field(name = 'ALL THE LINKS', value = message)
		await ctx.channel.send(embed = embed)
	except:
		await ctx.channel.send('NO LIST')

@client.command(aliases = [' del', 'del', 'rem' , 'remove'])
async def delete(ctx, number):
	with open('links.txt','r') as handle:
		links = handle.readlines()
	links.pop(int(number)-1)
	textfile = open("links.txt", "w")
	print(links)
	for element in links:
	    textfile.write(element)
	textfile.close()
	await ctx.channel.send('Deleted!')



@client.command(aliases = [' word'])
async def word(ctx, number,*, word):
	with open('links.txt','r') as handle:
		links = handle.readlines()
	thing = links[int(number)-1]
	run, link, notword = thing.split(' ', 2)
	links[int(number)-1] = run + ' ' + link + ' '+ word + '\n'
	textfile = open("links.txt", "w")
	for element in links:
	    textfile.write(element)
	textfile.close()
	await ctx.channel.send('Changed!')




@client.command(aliases = [' run', '  run', 'set'])
async def run(ctx, linknum, runornot):
	with open('links.txt','r') as handle:
		links = handle.readlines()
	setting = links[int(linknum)-1][:4]
	thing = links[int(linknum)-1][5:]
	if runornot == 'true':
		links[int(linknum)-1] = 'run=1' + thing
	elif runornot == 'false':
		links[int(linknum)-1] = 'run=0' + thing
	textfile = open("links.txt", "w")
	for element in links:
	    textfile.write(element)
	textfile.close()
	await ctx.channel.send('Changed!')


@client.command(aliases = [' start'])
async def start(ctx):
	here.start(ctx)

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






