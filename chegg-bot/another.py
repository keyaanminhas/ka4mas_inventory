import os 
import discord, re, requests, asyncio
from discord.ext import commands
from bs4 import BeautifulSoup
from mechanize import Browser

bot = discord.Client()

@bot.event
async def on_ready():   
    
    guild_count = 0
    for guild in bot.guilds:        
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    print("BOT is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):

    link = re.findall(r'(https?://[^\s]+)', message.content)
    check = '-ch ' + link[0]

    if(message.content == check):
        chegglink = link[0]
        try:
            if(chegglink[0:22] == "https://www.chegg.com/"):


                userRequest = requests.get(link[0],headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0",
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "cookie":"id_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1vaGxzaG9udHNtQGhvdG1haWwuY29tIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsInN1YiI6IjEwNWZkMjcyLWNjNDgtNDBlNS1hNjgzLTI4MjY0MTU4MmQzZSIsImF1ZCI6IkNIR0ciLCJpYXQiOjE2NTcwNTg4OTksImV4cCI6MTY3MjYxMDg5OSwicmVwYWNrZXJfaWQiOiJhcHcifQ.kARj-U3cM5kOV9osqMQByDXoAXPEFIbwYQSMwxTGdbMMju4Wkjw9oX3-B2_1GNIE3GIpVhloistdSUqR0OqODVpj90yaOd3cN4J5OWM_b_OsjNBGKt2C9YnHqgsK0jxwKlmipi4yLtZtFV6LCAunbOFhhaPFo4x4YEyRPZx9TJuQRAKQ3Ob5J9DZ7F3nOazKtP9eUUSQjkWafwthHSy8JiYz6zzG9Ef-WUaZBLInhV9f-2o6TW1ollikUirYQfpQU2WYPTPRVitXF9MJsEOOmUHUaoxAn7oNmjUvoitJkgJ0iRGFwXa3h5XN3RXD8xG8vZEbboXBZNy8D4osemJhEw"})

                source = BeautifulSoup(userRequest.content,"html")
                #source =(BeautifulSoup(userRequest.content, 'lxml'))
                print(source)
                dmain = source.find("div",attrs={"class":"answer-given-body ugc-base"})
                images = dmain.findAll('img')
                for image in images:
                    await message.author.send(image['src'])
                await message.author.send('-----------------------------------------------------')
                data = source.find("div",attrs={"class":"answer-given-body ugc-base"}).text
                file = open('answer.txt', 'w')   
                file.write(data)  
                file.close()
                my_files = [discord.File('answer.txt')]
                print(link[0])
                await message.author.send(files=my_files)
                exit(0)
            else:
                print("Link is not valid.")
        except ValueError:
            print("Unexpected value is given")
            exit(1)
        except ConnectionError as ex:
             raise RuntimeError('Failed to establish connection to the given soruce') from ex
            

bot.run("OTAwMzYwNTI1MTQwMDcwNDAw.YXAMFQ.YFWeeyP8o7e11rjP-Yy1B-883Cg")