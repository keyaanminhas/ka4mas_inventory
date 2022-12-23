import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions, CheckFailure
msg1 = '.'
msg2 = '.'
msg3 = '.'
msg4 = '.'
msg5 = '.'
msg6 = '.'
msg7 = '.'
client = commands.Bot(command_prefix = "key ")

@client.event
async def on_ready():
	print("STARTED")

@client.command(aliases=['rul', 'rules', 'ruless', 'ules', 'ule'])
async def rule(ctx, *, number):
	f = open('rules.txt', 'r')
	rules = f.readlines()
	if int(number) > len(rules):
		await ctx.send('Please choose a valid number')
	else:
		await ctx.send(rules[int(number) - 1])

@client.event
async def on_message_delete(message):
	if message.author == client.user:
		return
	elif (message.content).find('key snipe')==-1:
		print('stuck')
		global msg1
		global msg2
		global msg3
		global msg4
		global msg5
		global msg6
		global msg7
		msg7 = str(message.author) + " " + str(message.content)
		msg1 = msg2
		msg2 = msg3
		msg4 = msg5
		msg5 = msg6
		msg6 = msg7
	if (message.content).find('key snipe')!= -1:
		msg_content = message.content
		number = msg_content[-1]
		if number == '1':await message.channel.send(msg7)
		elif number == '2':await message.channel.send(msg6)
		elif number == '3':await message.channel.send(msg5)
		elif number == '4':await message.channel.send(msg4)
		elif number == '5':await message.channel.send(msg3)
		elif number == '6':await message.channel.send(msg2)
		elif number == '7':await message.channel.send(msg1)
		if number == '0':
			sen = ['1.' + msg7, '2.'+ msg6, '3.'+ msg5, '4.'+ msg4, '5.' + msg3, '6.'+ msg2, '7.'+msg1]
			for i in range(0, len(sen)-1):
				this = string(sen[i])
				await message.channel.send(this) 


@client.command(aliases=['clean'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit = amount + 1)

@client.command(aliases=['kcik'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, * ,reason = 'No reason provided'):
	await ctx.guild.kick(member, reason = reason)
	try:
		await member.send("You have been kicked!")
	except:
		print('closed dms')

@client.command(aliases = ['snip'])
async def snipe(ctx, number = 1):
	number = int(number)
	if number == 1:await ctx.send(msg7)
	elif number == 2:await ctx.send(msg6)
	elif number == 3:await ctx.send(msg5)
	elif number == 4:await ctx.send(msg4)
	elif number == 5:await ctx.send(msg3)
	elif number == 6:await ctx.send(msg2)
	elif number == 7:await ctx.send(msg1)
@client.command(aliases=['bna'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, * ,reason = 'No reason provided'):
	await member.ban(reason = reason)
	try:
		await member.send("You have been banned")
	except:
		print('closed dms')
client.run('ODkzODQwMTQzMzE4OTEzMDI0.YVhTgA.9Z0QkBhljUsB41zvugJDuwRt7Es')