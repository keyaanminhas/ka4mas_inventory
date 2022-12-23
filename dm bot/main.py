import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions, CheckFailure
import random
import requests
import asyncio




intents = discord.Intents.all()
intents.members = True

client = commands.Bot(intents=intents,command_prefix = ",")

client.remove_command('help')

client.intents.members = True

@client.event
async def on_ready():
	print("BOT IS STARTED")
	await client.change_presence(activity=discord.Game(name="Playing life"))

@client.command(aliases = [' dm'])
async def dm(ctx, *, message):
	done = []
	content = message
	for member in guild.members:
		try:
			if member not in done:
				dms = await member.create_dm()
				await dms.send(content)
				done.append(member)
		except:
			print('yeah')

client.run('OTE5NTUzMTA1MDIzMDc4NDYw.YbXekA.z34VRuUzHBAkvRO50I5oFqV0qyQ')

