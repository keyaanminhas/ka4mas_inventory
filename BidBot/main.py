import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import tasks
import random
import requests
import asyncio
import sqlite3
import time
from datetime import datetime
from datetime import date


global time, item, started, current_bet




client = commands.Bot(command_prefix = "!!") #MAIN CLIENT USED TO COMUNICATE WITH DISCORD

client.remove_command('help') #To create our own help command which is better than Default one :)

@client.event #Discord library's predefined-function which waits for activity
async def on_ready(): #When the bot becomes ready
	print("BOT IS STARTED") #Awares us that its started

	await client.change_presence(activity=discord.Game(name="AUCTIONEER")) #Presence or activity which makes it look cool


#HELP COMMAND

@client.command(aliases=[' help']) #Different key words to be considered the same
@commands.has_permissions(administrator=True) #Check if the user has administrator permission
async def help(ctx): #defining the function
	embed = discord.Embed(
		colour = discord.Color.random()
	) # Embed are a way to represent information on discord

	embed.set_author(name ='HELP')# Title of message
	#CONTENT OF MESSAGE
	embed.add_field(name = '!! help', value = 'SHOWS THIS COMMAND', inline=False)
	embed.add_field(name = '!! reset <user> <server> <expiry data>', value = 'RESETS THE BID', inline = False)
	embed.add_field(name = '!! start <Hours:Mins> <date> <starting bid> <item>', value = 'START A BID', inline = False)
	embed.add_field(name = '!! history', value = 'HISTORY OF BIDS', inline = False)
	embed.add_field(name = '!! stop', value = 'STOP THE BID', inline = False)
	embed.add_field(name = '!! status', value = 'DISPLAYS THE CURRENT BIDDER AND TIME LEFT', inline = False)

	await ctx.channel.send(embed=embed) #SENDING THE MESSAGE ON DISCORD


@client.command(aliases=[' work'])
@commands.has_permissions(administrator=True)
async def work(ctx, name:discord.User):
	print('working')
	print(name)

token = 'OTMwOTI4OTQ2OTI3Nzc1Nzc0.Yd9BJA.s2DEpBxJVlmlQeZ415PFSWHbO5c'
client.run(token)