import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions, CheckFailure
import random
import requests
import asyncio
import json
from wolframalpha import *





app_id = '4KR66T-9RU9Q7T5EX'
cli = Client(app_id)

cols = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D', 'E', 'F']



intents = discord.Intents.all()
intents.members = True

mykey = 'UTJIWLSPEEXVZH5LIEMSZB03N7SYBHLK'
client = commands.Bot(intents=intents,command_prefix = ",")

client.remove_command('help')

client.intents.members = True

@client.event
async def on_ready():
	print("BOT IS STARTED")
	await client.change_presence(activity=discord.Game(name="Playing life"))

@client.command(aliases = [' csgo'])
async def csgo(ctx):
	players = []
	csgo = []
	names = []
	for guild in client.guilds:
		for member in guild.members:
			if member not in players:
				try:
					if member not in csgo:
						csgo.append(member)
				except:
					print('error in this guy')
	embed = discord.Embed(
		title = "CSGO",
		colour = discord.Color.dark_green()
	)

	for cs in csgo:
		if cs.activities:
			for acts in cs.activities:
				if str(acts).find('Counter-Strike')!=-1:
					names.append(cs)

	try:
		embed.add_field(name = "NERDS PLAYING CSGO", value = len(names),inline = False)
		embed.add_field(name = "Names", value = ", ".join(map(str, names)), inline = True)
		embed.set_footer(text = "Press 'Y' to ping them all")
		await ctx.channel.send(embed=embed)
	except:
		await ctx.channel.send("None of the players are playing csgo.")



@client.command(aliases=[' help'])
async def help(ctx):
	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	embed.set_author(name ='HELP')
	embed.add_field(name = ',help', value = 'CALLS 911', inline=False)
	embed.add_field(name = ',kick', value = 'Kicks one of the poor members you mention', inline=False)
	embed.add_field(name = ',help', value = 'Ban a fellow homie', inline=False)
	embed.add_field(name = ',clear', value = 'Makes your chat holy again', inline=False)
	embed.add_field(name = ',joke', value= 'Tell you something not funny', inline= False)
	embed.add_field(name = ',roast', value = 'You wont be able to chat after this', inline = False)
	embed.add_field(name = ',cats', value = 'SEND A CATS PIC', inline = False)
	embed.add_field(name = ',aq OR ,anime quote', value = 'Anime lovers you need these (generates a quote)', inline = False)
	embed.add_field(name = ',search yourword', value = 'For those who not good at english', inline = False)
	embed.add_field(name = ',anime name <NameOfAnime>', value = 'Generates quote of mentioned anime', inline = False)
	embed.add_field(name = ',anime char <NameOfCharacter>', value = 'Generates a quote of anime character', inline = False)
	embed.add_field(name = ',poetry', value = 'Time to go deep', inline = False)
	embed.add_field(name = ',quote <Tag> OR = | AND = ,  example: ,qt love,friendship', value = 'Suicide is profitable trade with life. -Ka4ma', inline = False)
	embed.add_field(name = ',tags ', value = 'All the tags available for quotes', inline=False)
	embed.add_field(name = ',whois yourwebsite.com', value = 'Gathers details about the domain', inline=False)
	embed.add_field(name = ',creator', value = 'WHO AM I', inline=False)
	embed.add_field(name = ',question', value = 'Ill answer any question which has an answer', inline = False)

	await ctx.channel.send(embed=embed)



@client.command(aliases=[' clean', 'clean', ' clear'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit = amount + 1)


@client.command(aliases=[' kcik', 'kcik', ' kick'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, * ,reason = 'No reason provided'):
	await ctx.guild.kick(member, reason = reason)
	try:
		await member.send("You have been kicked!")
	except:
		print('closed dms')

@client.command(aliases=['bna', ' ban', ' bna'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, * ,reason = 'No reason provided'):
	await member.ban(reason = reason)
	try:
		await member.send("You have been banned")
	except:
		print('closed dms')

@client.command(aliases = [' roast', 'rst', 'raost', ' raost'])
async def roast(ctx):
	roast = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=text')
	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	embed.add_field(name = 'ROAST', value = str(roast.text), inline=False)

	await ctx.channel.send(embed=embed)


@client.command(aliases = [' joke', 'jk', 'joek', ' joek'])
async def joke(ctx):
	joke = requests.get('https://v2.jokeapi.dev/joke/Any?format=txt')
	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	embed.add_field(name = 'JOKE', value = str(joke.text), inline=False)

	await ctx.channel.send(embed=embed)


@client.command(aliases = [' cat', 'cta', 'cata', ' cta', 'cats', ' cats', 'pussy', ' pussy', ' pussycat', 'pussycat'])
async def cat(ctx):
	cat = requests.get('https://aws.random.cat/meow')
	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	data = json.loads(cat.text)["file"]
	embed.add_field(name = 'CATS', value = 'Cute', inline=False)
	embed.set_image(url = (str(data)))

	await ctx.channel.send(embed=embed)


@client.command(aliases = [' anime quote', ' anime quotee', 'anime quote', ' aq', 'aq'])
async def anime(ctx):
	anime = requests.get('https://animechan.vercel.app/api/random')
	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	fromm = json.loads(anime.text)["anime"]
	character = json.loads(anime.text)["character"]
	quote = json.loads(anime.text)["quote"]

	embed.add_field(name = 'From:', value = fromm, inline=False)
	embed.add_field(name = 'Said By:', value = character, inline=False)
	embed.add_field(name = 'QUOTE:', value = quote, inline=False)
	await ctx.channel.send(embed=embed)


@client.command(aliases = [' anime char', 'anime char', ' ac', 'anime character'])
async def ac(ctx, * , message):
	anime = requests.get(f'https://animechan.vercel.app/api/quotes/character?name={message}')
	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	data = anime.json()
	try:
		number = random.randint(0, len(data)-1)
		fromm = data[number]["anime"]
		character = data[number]["character"]
		quote = data[number]["quote"]
		embed.add_field(name = 'From:', value = fromm, inline=False)
		embed.add_field(name = 'Said By:', value = character, inline=False)
		embed.add_field(name = 'QUOTE:', value = quote, inline=False)
		await ctx.channel.send(embed=embed)
	except:
		await ctx.channel.send('No quote of the personality or some other error')	




@client.command(aliases = [' anime name', 'anime name', ' an', 'anime nme'])
async def an(ctx, *, message):
	anime = requests.get(f'https://animechan.vercel.app/api/quotes/anime?title={message}')
	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	data = anime.json()
	try:
		number = random.randint(0, len(data)-1)
		fromm = data[number]["anime"]
		character = data[number]["character"]
		quote = data[number]["quote"]
		embed.add_field(name = 'From:', value = fromm, inline=False)
		embed.add_field(name = 'Said By:', value = character, inline=False)
		embed.add_field(name = 'QUOTE:', value = quote, inline=False)
		await ctx.channel.send(embed=embed)
	except:
		await ctx.channel.send('No quote of the anime or some other error')




@client.command(aliases = [' poetry', 'peotry', ' peorty', 'potry'])
async def poetry(ctx):
	done = False
	with open('writers.txt') as f:
	    writers = f.read().splitlines() 

	writer = random.choice(writers)

	r = requests.get(f'https://poetrydb.org/author/{writer}/title')

	data = r.json()
	while done != True:
		try:
			title = data[random.randint(0, len(data)-1)]['title']


			response = requests.get(f'https://poetrydb.org/author,title/{writer};{title}')

			data = response.json()

			title = data[0]['title']
			author = data[0]['author']
			lines = data[0]['lines']
			x = ("\n".join(lines))
			embed = discord.Embed(
				colour = random.randint(0, 255)
			)
			embed.add_field(name = 'Title:', value = title, inline=False)
			embed.add_field(name = 'Author:', value = author, inline=False)
			embed.add_field(name = 'Poetry:', value = x, inline=False)
			await ctx.channel.send(embed=embed)
			done = True
		except:
			pass



@client.command(aliases = [' search', ' serch', 'serch', ' saerch', 'saerch'])
async def search(ctx, * ,word):
	headers = {'Authorization': 'token 81e89d34d6e4f04d2d7f19e1729234985fd821d6'}
	response = requests.get(f'https://owlbot.info/api/v4/dictionary/{word}', headers = headers)


	jresp = json.loads(response.text)['definitions']
	pronounce = json.loads(response.text)['pronunciation']

	data = jresp[0]
	tpye = data['type']
	defi = data['definition']
	egz = data['example']
	img = data['image_url']

	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	embed.set_author(name = str(word).upper())
	embed.add_field(name = 'TYPE: ', value = tpye, inline = False)
	embed.add_field(name = 'PRONUNCIATION: ', value = pronounce, inline = False)
	embed.add_field(name = 'DEFINITION: ', value = defi, inline = False)
	embed.add_field(name = 'EXAMPLE: ', value = egz, inline = False)
	if str(img).lower() != 'none':
		embed.set_image(url = img)

	await ctx.channel.send(embed=embed)


@client.command(aliases = [' ip'])
async def ip(ctx):
	try:
		ip = myip()
		req = requests.get(url + f'/give?ip={ip}')
		print(req.content)
	except:
		print('error')





@client.command(aliases = [' quote', ' qt', 'qt', ' qute', 'qoute'])
async def quote(ctx, *, tags = '<<<>>>'):
	if tags == '<<<>>>':
		response = requests.get(f'http://api.quotable.io/random')
	else:
		response = requests.get(f'http://api.quotable.io/random?tags={tags}')
	data = response.json()
	try:
		tags = data['tags']
		date = data['dateAdded']
		content = data['content']
		author = data['author']
	except:
		await ctx.channel.send("That tag doesnt exist")

	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	embed.add_field(name = 'QUOTE:', value = '"' + content + '"' + f' -{author}', inline = False)
	embed.add_field(name = "DATE", value = date, inline = False)
	embed.set_footer(text = ' '.join(map(str, tags)))
	await ctx.channel.send(embed=embed)


@client.command(aliases = [' tags', ' tgs', 'tag'])
async def tags(ctx):
	response = requests.get('http://api.quotable.io/tags')
	data = response.json()
	embed = discord.Embed(
		colour = random.randint(0, 255)
	)
	for i in data:
		embed.add_field(name = i["name"], value = f'Quote Count = {i["quoteCount"]}')

	await ctx.channel.send(embed=embed)



@client.command(aliases = [' who is', ' whois', 'who is'])
async def whois(ctx, *, domain_name):
	response = requests.get(f"https://api.ip2whois.com/v2?key={mykey}&domain={domain_name}")
	parsed = json.loads(response.text)

	with open("results.txt", "w") as file:
		file.write(json.dumps(parsed, indent=4, sort_keys=True))

	with open("results.txt", "rb") as file:
		await ctx.channel.send("Website lookup results: ", file=discord.File(file, "results.txt"))

@client.command(aliases = [' creator'])
async def creator(ctx):
	embed = discord.Embed(title="To Hire Me",
		url = 'https://www.fiverr.com/ka4ma_coder',
		color = discord.Color.red())
	embed.set_author(name = "Ka4ma", icon_url='https://cdn.discordapp.com/avatars/693533573105451089/5c5616f3952648c5ce10908266e52779.webp?size=512')
	embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/799613453529645079/909403807962783754/unknown.png')
	embed.add_field(name = "Me...", value = '''Not too old not to gold.
I am an intermediate PYTHON programmer.''', inline = True)
	embed.add_field(name = 'Speciality', value= 'Web automation and bots are kinda my thing.', inline = True)
	embed.add_field(name = 'Improving me', value= 'And also if you have any suggestions or anything related or not related my dms are open to all.', inline = False)
	embed.set_footer(text = '\n"Suicide is a profitable trade with life." -Ka4ma')
	embed.set_image(url = 'https://cdn.discordapp.com/attachments/799613453529645079/909409097382764544/unknown.png')
	await ctx.channel.send(embed=embed)

@client.command(aliases = [' , question'])
async def question(ctx, *,  que):
	embed = discord.Embed(
	color = discord.Color.random())

	try:
		res = cli.query(que)
		text = ''

		for pod in res.pods:
		    for sub in pod.subpods:
		    	text = text + sub.plaintext

		
		embed.add_field(name = 'Answer', value = text)
		await ctx.channel.send(embed=embed)
	except:
		await ctx.channel.send("Your question wasnt found")




client.run('OTA2ODExNjc4Njk4NjQzNTI3.YYeELw.Fq07IBBJ7bXPK1af4qc1K4_AuFQ')
