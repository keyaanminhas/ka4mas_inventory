import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions, CheckFailure
import random
import requests
import asyncio
import sqlite3
import time
from datetime import date
import datetime






client = commands.Bot(command_prefix = "..") #MAIN CLIENT USED TO COMUNICATE WITH DISCORD

client.remove_command('help') #To create our own help command which is better than Default one :)
global conn, c

#DATABASE CODE

def remove_this(name, field):
	global conn, c
	command = f"UPDATE customers SET {field} = NULL where name IN('{name}')"
	with conn:
		c.execute(command)

def add_data(name, field, date):
	global conn, c
	with conn:
		try:
			command = f"INSERT INTO customers (name, {field}) VALUES ('{name}', '{date}')"
			c.execute(command)
		except:
			command = f"UPDATE customers SET {field} = '{date}' where name IN('{name}')"
			c.execute(command)


def search_name(name):
	global conn, c
	with conn:
		c.execute("SELECT * FROM customers WHERE name=?", (name,))
		return c.fetchone()

def remove_row(name):
	global conn, c
	with conn:
		c.execute("DELETE from customers WHERE name=?", (name,))

def all_data():
	global conn, c
	with conn:
		c.execute("SELECT * FROM customers")
		return c.fetchall()

def new_name(field, user):
	index = 0
	global conn, c
	name = field
	field = field + '1'
	leng = len(name)
	with conn:
		while True:
			try:
				command = f"SELECT {field} FROM customers"
				c.execute(command)
				res = search_name(user)
				print(res)
				columns = get_columns()
				for i in range(len(columns)):
					column = columns[i]
					if column[0] == field:
						index = i
				print(res[index])
				if res[index] == None:
					return field

				if field == name:
					field = field + str(1)
				else:
					print(str(int(field[leng:])))
					field = field[:leng] + str(int(field[leng:]) + 1)
			except:
				return field

				








def add_column(field):
	global conn, c
	try:
		command = f"SELECT {field} FROM customers"
		c.execute(command)
		conn.commit()
	except:
		command = f"ALTER TABLE customers ADD COLUMN {field} varchar(32)"
		c.execute(command)
		conn.commit()

def remove_column(field):
	global conn, c
	try:
		with conn:
			command = f"ALTER TABLE customers DROP COLUMN {field}"
			c.execute(command)
	except:
		return 'field doesnt exist'

def get_columns():
	global conn, c
	try:
		with conn:
			command = "SELECT name FROM pragma_table_info('customers')"
			c.execute(command)
			data = c.fetchall()
			return data
	except:
		return "Table doesnt exist"






#BEGINNING OF CODE

@client.event #Discord library's predefined-function which waits for activity
async def on_ready(): #When the bot becomes ready
	print("BOT IS STARTED") #Awares us that its started
	global conn, c
	conn = sqlite3.connect('data.db')

	c = conn.cursor()

	c.execute("""CREATE TABLE IF NOT EXISTS customers (
			id integer PRIMARY KEY AUTOINCREMENT,
			name text UNIQUE
	);""")
	await client.change_presence(activity=discord.Game(name="DATABASE")) #Presence or activity which makes it look cool


#HELP COMMAND

@client.command(aliases=[' help']) #Different key words to be considered the same
@commands.has_permissions(administrator=True) #Check if the user has administrator permission
async def help(ctx): #defining the function
	embed = discord.Embed(
		colour = discord.Color.random()
	) # Embed are a way to represent information on discord

	embed.set_author(name ='HELP')# Title of message
	#CONTENT OF MESSAGE
	embed.add_field(name = '..help', value = 'SHOWS THIS COMMAND', inline=False)
	embed.add_field(name = '..add <user> <server> <expiry data>', value = 'ADDS A USER TO A SERVER', inline = False)
	embed.add_field(name = '..list <user>', value = 'DISPLAYS YOUR SUBSCRIBED SERVERS', inline = False)
	embed.add_field(name = '..remove user <user>', value = 'REMOVES ALL THE USERS DATA', inline = False)
	embed.add_field(name = '..remove server <number>', value = 'REMOVES THE SERVER FROM ALL USERS', inline = False)
	embed.add_field(name = '..remove <name_of_server> <number>', value = 'REMOVE THE SERVER WITH THE NAME AND NUMBER', inline = False)

	await ctx.channel.send(embed=embed) #SENDING THE MESSAGE ON DISCORD

@client.command(aliases=[' add'])
@commands.has_permissions(administrator=True)
async def add(ctx, name:discord.User,  field, date):
	await ctx.channel.purge(limit = 1)
	add_column(field)
	new = new_name(field ,name)
	add_column(new)
	add_data(name, new, date)
	await ctx.channel.send("Added!")

@client.command(aliases=[' whois'])
@commands.has_permissions(administrator=True)
async def whois(ctx, name:discord.User):
	print(name)
	await ctx.channel.send(ctx.message.author)
	await ctx.channel.send(name.mention)


@client.command(aliases=[' remove'])
@commands.has_permissions(administrator=True)
async def remove(ctx, name,  field, number):
	await ctx.channel.purge(limit = 1)
	field = field + str(number)
	remove_this(name, field)
	await ctx.channel.send("Removed!")


@client.command(aliases=[' listme'])
async def listme(ctx):
	d = ctx.message.author
	name = d
	name = str(name)
	today = date.today()
	user_info = search_name(name)
	subed_servers = []
	dates = []
	exps = []
	servers = get_columns()
	servers = servers[2:]
	try:
		user_info = user_info[2:]

		for i in range(0,len(user_info)):
			if user_info[i] != None:
				server_to_add = servers[i]
				server_to_add = str(server_to_add)
				server_to_add = server_to_add[2:-3]
				subed_servers.append(server_to_add)
				dates.append(user_info[i])
				comp_date = user_info[i]
				exp_or_not = datetime.datetime(int(comp_date[-4:]), int(comp_date[3:5]) , int(comp_date[0:2]))
				date_time = datetime.datetime.combine(today, datetime.time(0, 0))
				if date_time > exp_or_not:
					exps.append('EXPIRED!')
				else:
					exps.append('EXPIRY!')
	except:
		pass
	message = f"""USER {name} is currently subscribed to:
"""
	for i in range(0, len(subed_servers)):
		noint = ''
		ints = ''
		for x in subed_servers[i]:
			try:
				int(x)
				ints = str(x)
			except:
				noint = noint + x

		message = message + f"""{ints}. {noint.upper()} - {exps[i]} - {dates[i]}\n"""

	await d.send(message)



@client.command(aliases=['removeuser'])
@commands.has_permissions(administrator=True)
async def remove_user(ctx, name):
	await ctx.channel.purge(limit = 1)
	remove_row(name)
	await ctx.channel.send("Removed!")


@client.command(aliases=['removeserver'])
@commands.has_permissions(administrator=True)
async def remove_server(ctx, field):
	await ctx.channel.purge(limit = 1)
	remove_column(field)
	await ctx.channel.send(f"Removed the {field}!")




@client.command(aliases=[' list'])
@commands.has_permissions(administrator=True)
async def list(ctx, name):
	await ctx.channel.purge(limit = 1)
	today = date.today()
	user_info = search_name(name)
	subed_servers = []
	dates = []
	exps = []
	servers = get_columns()
	servers = servers[2:]
	try:
		user_info = user_info[2:]

		for i in range(0,len(user_info)):
			if user_info[i] != None:
				server_to_add = servers[i]
				server_to_add = str(server_to_add)
				server_to_add = server_to_add[2:-3]
				subed_servers.append(server_to_add)
				dates.append(user_info[i])
				comp_date = user_info[i]
				exp_or_not = datetime.datetime(int(comp_date[-4:]), int(comp_date[3:5]) , int(comp_date[0:2]))
				date_time = datetime.datetime.combine(today, datetime.time(0, 0))
				if date_time > exp_or_not:
					exps.append('EXPIRED!')
				else:
					exps.append('EXPIRY!')
	except:
		pass
	message = f"""USER {name} is currently subscribed to:
"""
	for i in range(0, len(subed_servers)):
		noint = ''
		ints = ''
		for x in subed_servers[i]:
			try:
				int(x)
				ints = str(x)
			except:
				noint = noint + x

		message = message + f"""{ints}. {noint.upper()} - {exps[i]} - {dates[i]}\n"""

	await ctx.channel.send(message)




token = 'OTI5ODAyMTU0MzA1MjgyMTQ4.YdsnvA.myL1kyN46_jTDIH3gc88uzSj38E'
client.run(token)